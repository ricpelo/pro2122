import dinero.Cuenta;
import personas.Cliente;

public class Principal {
    public static void main(String[] args) {
        Cliente manuel = new Cliente("48673254J", "Manuel González");
        Cliente juan = new Cliente("dlkjflks", "Juan");
        Cliente maria = new Cliente("2131312", "María");
        Cuenta c1 = new Cuenta(1);

        c1.insertarTitular(manuel)
                .insertarTitular(juan)
                .insertarTitular(maria);

        try {
            c1.quitarTitular(5);
            c1.mostrarTitulares();
        } catch (IndexOutOfBoundsException e) {
            System.err.println(e.getMessage());
        }
    }
}
