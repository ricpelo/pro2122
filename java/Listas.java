import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Listas {
    public static void main(String[] args) {
        ArrayList l = new ArrayList(25);

        l.add(24);
        l.add(73.0);
        l.add("Hola");
        l.trimToSize();
        System.out.println(l.size());
    }
}
