public class Principal {
    public static void main(String[] args) {
        Ballena gris = new Ballena();
        Ave canario = new Ave();
        CantorNadador ariel = new Sirena();
        cantaYNada(gris);
        cantar(ariel);
        gris.cantar();
    }

    public static void cantaYNada(CantorNadador x) {
        x.canta();
        x.nada();
    }

    public static void cantar(Cantor c) {
        c.canta();
    }
}
