import dinero.Cuenta;
import personas.Cliente;
import personas.Menor;

public class Principal {
    public static void main(String[] args) {
        Cliente manuel = new Cliente("48673254J", "Manuel González");
        Cliente juan = new Cliente("dlkjflks", "Juan");
        Cliente maria = new Cliente("2131312", "María");
        Menor pepito = new Menor("123123M", "Pepito", manuel);
        Cuenta c1 = new Cuenta(1);

        System.out.println(pepito);

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
