public class Triangulo extends Figura implements BaseAltura {
    private double base;
    private double altura;

    public Triangulo(double base, double altura) {
        setBase(base);
        setAltura(altura);
    }

    @Override
    public double getBase() {
        return base;
    }

    public void setBase(double base) {
        this.base = base;
    }

    @Override
    public double getAltura() {
        return altura;
    }

    public void setAltura(double altura) {
        this.altura = altura;
    }

    @Override
    public double area() {
        return getBase() * getAltura() / 2.0;
    }
}
