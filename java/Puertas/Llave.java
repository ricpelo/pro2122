public class Llave {
    private String color;

    public Llave(String color) {
        if (color == null) {
            throw new IllegalArgumentException("El color no puede ser nulo");
        }
        this.color = color;
    }

    public String color() {
        return color;
    }
}
