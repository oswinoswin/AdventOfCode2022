public  abstract class Monkey {
    String name;
    Monkey left;
    Monkey right;

    public abstract long yell();


    public void preOrderTraversal(){
        System.out.println(this);
        if (left != null) left.preOrderTraversal();
        if (right != null) right.preOrderTraversal();
    }




}
