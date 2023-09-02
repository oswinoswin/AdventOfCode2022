public class NumberMonkey extends Monkey{
    long number;
    public NumberMonkey(String name, long value) {
        this.name = name;
        this.number = value;
    }

    @Override
    public long yell(){
        return number;
    }

    @Override
    public String toString() {
        return name + " -> " + number;
    }
}
