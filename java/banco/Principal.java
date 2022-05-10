import dinero.Cuenta;
import interfaces.Numerable;
import personas.Adulto;
import personas.Menor;

public class Principal {
    public static void main(String[] args) {
        Adulto manuel = new Adulto("48673254J", "Manuel González");
        Adulto juan = new Adulto("dlkjflks", "Juan");
        Adulto maria = new Adulto("2131312", "María");
        Menor pepito = new Menor("123123M", "Pepito", manuel);
        Cuenta c1 = new Cuenta(1L);

        System.out.println(pepito);
        mostrarNumero(manuel);
        mostrarNumero(c1);

        // c1.insertarTitular(manuel)
        //         .insertarTitular(juan)
        //         .insertarTitular(maria);

        // try {
        //     c1.quitarTitular(5);
        //     c1.mostrarTitulares();
        // } catch (IndexOutOfBoundsException e) {
        //     System.err.println(e.getMessage());
        // }
    }

    public static void mostrarNumero(Numerable n) {
        System.out.println(n.getNumero());
    }
}
