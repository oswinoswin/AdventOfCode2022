import java.util.function.BinaryOperator;
import java.util.function.Function;

public class OperationMonkey extends Monkey{
    public BinaryOperator<Long> operation;
    String operationString;

    public OperationMonkey(String name, String operationString) {
        this.name = name;
        this.operationString = operationString;
        switch (operationString){
            case "+" -> operation = (x, y) -> x + y;
            case "-" -> operation = (x, y) -> x - y;
            case "*" -> operation = (x, y) -> x * y;
            case "/" -> operation = (x, y) -> x / y;
            default -> throw new IllegalStateException("Unexpected value: " + operationString);
        }

    }

    @Override
    public long yell() {
        long leftValue = left.yell();
        long rightValue = right.yell();
        return operation.apply(leftValue, rightValue);
    }

    @Override
    public String toString() {
        return name + " -> " + left.name +" " + operationString + " " + right.name;
    }


}
