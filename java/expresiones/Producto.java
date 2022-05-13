public class Producto extends Expresion {
    private Expresion x;
    private Expresion y;

    public Producto(Expresion x, Expresion y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int valor() {
        return x.valor() * y.valor();
    }
}
