public class Principal {
    public static void main(String[] args) {
        Triangulo t = new Triangulo(3.0, 4.0);
        Cuadrado c = new Cuadrado(7.0);
        Circulo ci = new Circulo(3.25);

        System.out.println(t.area());
        System.out.println(c.area());
        System.out.println(calcularPerimetro(ci));
    }

    public static double calcularPerimetro(PoligonoRegular pr) {
        return pr.getLongSegmento() * pr.getNumSegmentos();
    }
}
