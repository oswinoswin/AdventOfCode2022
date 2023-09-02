import java.util.HashMap;
import java.util.Map;

public class MonkeyTree {
    Monkey root;
    Map<String, Monkey> leftKids; //kid name is key, parent is Monkey
    Map<String, Monkey> rightKids; //kid name is key, parent is monkey
    Map<String, Monkey> orphans;  //orphan name is the key
    public MonkeyTree() {
        leftKids = new HashMap<>();
        rightKids = new HashMap<>();
        orphans = new HashMap<>();
    }

    public void setRoot(Monkey root, String leftKid, String rightKid) {
        this.root = root;
        checkIfKidsExists(root, leftKid, rightKid);

    }

    public void addMonkey(Monkey monkey){
        if (leftKids.containsKey(monkey.name)){
            Monkey parent = leftKids.get(monkey.name);
            parent.left = monkey;
            leftKids.remove(monkey.name);
        } else if (rightKids.containsKey(monkey.name)) {
            Monkey parent = rightKids.get(monkey.name);
            parent.right = monkey;
            rightKids.remove(monkey.name);
        } else {
            orphans.put(monkey.name, monkey);
        }
    }



    public void checkIfKidsExists(Monkey monkey, String left, String right){
        //left kid first
        if (orphans.containsKey(left)){
            Monkey leftKid = orphans.get(left);
            monkey.left = leftKid;
            orphans.remove(left);
        } else {
            leftKids.put(left, monkey);
        }

        if (orphans.containsKey(right)){
            Monkey rightKid = orphans.get(right);
            monkey.right = rightKid;
            orphans.remove(right);
        } else {
            rightKids.put(right, monkey);
        }

    }

}
