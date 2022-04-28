import dinero.Cuenta;
import personas.Cliente;

public class Principal {
    public static void main(String[] args) {
        Cliente pepe = new Cliente("48673254J", "Manuel González");
        Cuenta c1 = new Cuenta(1, new Cliente[] { pepe });
        //
    }
}
