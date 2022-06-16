import java.util.NoSuchElementException;

public class PrincipalPila {
    public static void main(String[] args) {
        Pila<Integer> p = new Pila<>();

        try {
            System.out.println(p.esVacia());
            p.meter(5);
            p.meter(7);
            p.meter(2);
            System.out.println(p.cima());
            System.out.println(p.sacar());
            System.out.println(p.cima());
            p.sacar();
            p.sacar();
            p.sacar();
        } catch (NoSuchElementException e) {
            System.out.println("Me he pasado...");
        }
    }
}
