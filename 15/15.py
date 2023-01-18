import math
import re
import numpy as np


class Sensor:
    def __init__(self, nums):
        self.sensor_x = int(nums[0])
        self.sensor_y = int(nums[1])
        self.beacon_x = int(nums[2])
        self.beacon_y = int(nums[3])
        self.manhattan_dist_to_beacon = self.calculate_manhattan_dist_to_beacon()

    def calculate_manhattan_dist_to_beacon(self):
        return abs(self.sensor_x - self.beacon_x) + abs(self.sensor_y - self.beacon_y)

    def calculate_taken_positions_in_row(self, row):
        if self.calculate_manhattan_dist_to_beacon() - abs(row - self.sensor_y) < 0:
            return 0
        return (self.calculate_manhattan_dist_to_beacon() - abs(row - self.sensor_y)) * 2 + 1

    def calculate_taken_indexes(self, row):
        if self.calculate_taken_positions_in_row(row) == 0:
            return []
        dist = self.calculate_manhattan_dist_to_beacon() - abs(row - self.sensor_y)
        return [self.sensor_x - dist, self.sensor_x + dist]

    def __str__(self):
        return f"{self.__dict__}"


def first(filename, interesting_y):
    min_x = math.inf
    max_x = - math.inf
    taken_positions = []
    beacons_x = set()
    with open(filename, "r") as f:
        for line in f:
            nums = re.findall(r'-?[0-9]+', line)
            sensor = Sensor(nums)
            pos = sensor.calculate_taken_indexes(interesting_y)
            if pos:
                taken_positions.append(pos)
            if int(nums[3]) == interesting_y:
                beacons_x.add(int(nums[2]))
    for x_1, x_2 in taken_positions:
        if x_1 < min_x:
            min_x = x_1
        if x_2 > max_x:
            max_x = x_2

    for b_x in beacons_x:
        if b_x > max_x:
            max_x = b_x
        if b_x < min_x:
            min_x = b_x

    interesting_row = np.zeros(max_x - min_x + 1)
    for x_1, x_2 in taken_positions:
        for i in range(x_1, x_2 + 1):
            interesting_row[i - min_x] = 1
    for b_x in beacons_x:
        interesting_row[b_x - min_x] = 0
    return sum(interesting_row)


def second(filename, search_size):
    # przejrzeć wszystkie cords in [0, 4000000] |  w examle:[0, 20]
    # znaleźć jeden punkt gdzie nie ma beacoba ani zasięgu
    # zwrócić 4000000 *x + y

    min_x, max_x = 0, search_size + 1
    min_y, max_y = 0, search_size + 1


    beacons = [[] for _ in range(max_y)]
    sensors = []

    with open(filename, "r") as f:
        for line in f:
            nums = re.findall(r'-?[0-9]+', line)
            sensor = Sensor(nums)
            sensors.append(sensor)
            beacon_x = int(nums[2])
            beacon_y = int(nums[3])
            if beacon_y > max_x or beacon_x > max_x or beacon_y < 0 or beacon_x < 0:
                continue
            if beacon_x not in beacons[beacon_y]:
                beacons[beacon_y].append(beacon_x)
            # print(sensor)
    # print(beacons)
    for row in range(max_y - 1, -1, -1):
        print(row)
        row_area = np.ones(max_x) #odwrotnie niż w first
        for sensor in sensors:
            positions = sensor.calculate_taken_indexes(row)
            if positions:
                left, right = positions
                left = max(0, left)
                right = min(max_x, right)
                row_area[left:right + 1] = 0
        for beacon_x in beacons[row]:
            row_area[beacon_x] = 0

        if row_area.sum() == 1:
            print(f"GOT SOLUTION!")
            x = np.transpose((row_area > 0).nonzero())[0, 0]
            return x * 4000000 + row



# 4692643 is too low
# negative nums in input XD -? solved this
if __name__ == "__main__":
    # print(first("example.txt", 10))
    # print(first("input.txt", 2000000))
    print(second("example.txt", 20))
    print(second("input.txt", 4000000))
