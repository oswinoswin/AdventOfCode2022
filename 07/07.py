class FileNode:
    def __init__(self, name: str, file_size: int):
        self.name: str = name
        self.file_size: int = file_size

    def __str__(self):
        return f"FileNode: ({self.name},{self.file_size})"


class DirectoryNode:
    def __init__(self, name: str, parent_dir):
        self.parent_dir = parent_dir
        self.name: str = name
        self.dir_size: int = 0
        self.children_directories: list[DirectoryNode] = []
        self.files: list[FileNode] = []

    def add_file(self, file_to_add: FileNode):
        self.files.append(file_to_add)

    def add_directory(self, directory):
        self.children_directories.append(directory)

    def calculate_filesystem_size(self) -> int:
        tmp_size = 0
        for file in self.files:
            tmp_size += file.file_size

        for child_dir in self.children_directories:
            tmp_size += child_dir.calculate_filesystem_size()

        self.dir_size = tmp_size
        return self.dir_size

    def find_smol_directories(self, smol_dirs_list: list):
        if self.dir_size == 0:
            self.calculate_filesystem_size()
        smol_size = 100000

        for child_dir in self.children_directories:
            child_dir.find_smol_directories(smol_dirs_list)

        if self.dir_size <= smol_size:
            smol_dirs_list.append(self)

        return smol_dirs_list

    def find_directories_bigger_than(self, space_needed: int, big_dirs_list: list):
        if self.dir_size == 0:
            self.calculate_filesystem_size()

        for child_dir in self.children_directories:
            child_dir.find_directories_bigger_than(space_needed, big_dirs_list)

        if self.dir_size >= space_needed:
            big_dirs_list.append(self)

        return big_dirs_list

    def go_to_parent(self):
        return self.parent_dir

    def go_to_child(self, child_name: str):
        for dir_node in self.children_directories:
            if dir_node.name == child_name:
                return dir_node

    def __str__(self):
        files_str = "".join(f"{fn} " for fn in self.files)
        children_str = "".join(f"{x} " for x in self.children_directories)
        result = f"DirectoryNode: {self.name} size: {self.dir_size} " \
                 f"files: {files_str} " \
                 f"children directories: {children_str}"
        return result


def parse_input(filename: str):
    root = DirectoryNode("/", None)
    current_node = root
    with open(filename, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break

            if line.startswith("$ cd "):
                dir_to_go = line[5:]
                if dir_to_go.startswith("/"):
                    current_node = root

                elif dir_to_go.startswith(".."):
                    current_node = current_node.go_to_parent()

                else:
                    current_node = current_node.go_to_child(dir_to_go)

            elif line.startswith("$ ls"):
                while True:
                    f_position = f.tell()
                    line = f.readline()
                    if not line:
                        break
                    if line.startswith("$"):
                        f.seek(f_position)
                        break

                    if line.startswith("dir"):
                        dir_name = line[4:]
                        child_dir = DirectoryNode(dir_name, current_node)
                        current_node.add_directory(child_dir)

                    else:
                        file_size, file_name = line.split(" ")
                        file_size = int(file_size)
                        new_file = FileNode(file_name, file_size)
                        current_node.add_file(new_file)

    root.calculate_filesystem_size()
    return root


def first(filename):
    root = parse_input(filename)
    print(f"Root at the end: {root}")
    smol_dirs = root.find_smol_directories([])
    return sum(x.dir_size for x in smol_dirs)


def second(filename):
    root = parse_input(filename)
    total_disk_space = 70000000
    required_space = 30000000
    used_space = root.dir_size
    unused_space = total_disk_space - used_space
    space_needed = required_space - unused_space

    big_dirs = root.find_directories_bigger_than(space_needed, [])
    big_dirs.sort(key=lambda big_dir: big_dir.dir_size)
    return big_dirs[0].dir_size


if __name__ == "__main__":
    print(first("example.txt"))
    print(first("input.txt"))
    print(second("example.txt"))
    print(second("input.txt"))
