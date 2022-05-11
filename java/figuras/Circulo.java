public class Circulo extends Figura implements PoligonoRegular {
    private double radio;

    public Circulo(double radio) {
        setRadio(radio);
    }

    public double getRadio() {
        return radio;
    }

    public void setRadio(double radio) {
        this.radio = radio;
    }

    @Override
    public double area() {
        return Math.PI * Math.pow(getRadio(), 2.0);
    }

    @Override
    public int getNumSegmentos() {
        return 1;
    }

    @Override
    public double getLongSegmento() {
        return 2 * Math.PI * getRadio();
    }
}
