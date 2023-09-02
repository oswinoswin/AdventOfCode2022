import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.function.Function;

public class Main {

    public static void main(String[] args){
        String fileName = "input.txt";
        File file = new File(fileName);
        
        MonkeyTree monkeyTree = new MonkeyTree();

        try (Scanner scanner = new Scanner(file)) {
            while (scanner.hasNext()) {
                String line = scanner.nextLine().strip();
                String name = line.split(":")[0];
                String operationString = line.split(":")[1].strip();
//                System.out.println(name +" "+ operation);
//                Monkey monkey = new Monkey(name, operation);


                if (operationString.length() < 10){ //leaf
                    long value = Long.valueOf(operationString);
                    //NumberMonkey
                    Monkey monkey = new NumberMonkey(name, value);
                    monkeyTree.addMonkey(monkey);

                }

                else {
                    //operation monkey
                    String left = operationString.substring(0,4);
                    String right = operationString.substring(7, 11);
                    String op = operationString.substring(5, 6);

                    Monkey monkey = new OperationMonkey(name, op);

                    if ("root".equals(name)){
                        monkeyTree.setRoot(monkey, left, right);
                        continue;
                    }

                    monkeyTree.addMonkey(monkey);
                    monkeyTree.checkIfKidsExists(monkey, left, right);

                }
            }

            monkeyTree.root.preOrderTraversal();
            System.out.println(monkeyTree.root.yell());

        } catch (FileNotFoundException e) {
            System.out.println("No file found: " + fileName);
        }
    }
}
