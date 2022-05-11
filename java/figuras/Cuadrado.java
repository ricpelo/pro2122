public class Cuadrado extends Figura implements BaseAltura, PoligonoRegular {
    private double longLado;

    public Cuadrado(double longLado) {
        setLongLado(longLado);
    }

    public double getLongLado() {
        return longLado;
    }

    public void setLongLado(double longLado) {
        this.longLado = longLado;
    }

    @Override
    public double area() {
        return getLongLado() * getLongLado();
    }

    @Override
    public double getBase() {
        return getLongLado();
    }

    @Override
    public double getAltura() {
        return getLongLado();
    }

    @Override
    public int getNumSegmentos() {
        return 4;
    }

    @Override
    public double getLongSegmento() {
        return getLongLado();
    }
}
