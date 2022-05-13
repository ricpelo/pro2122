public class Suma extends Expresion {
    private Expresion x;
    private Expresion y;

    public Suma(Expresion x, Expresion y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int valor() {
        return x.valor() + y.valor();
    }
}
