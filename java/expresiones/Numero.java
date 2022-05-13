public class Numero extends Expresion {
    private int numero;

    public Numero(int x) {
        numero = x;
    }

    @Override
    public int valor() {
        return numero;
    }
}
