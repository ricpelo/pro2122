enum EstadoPuerta {
    ABIERTA, CERRADA
}

public class Puerta {
    private String color;
    private EstadoPuerta estado;
    private Llave llave;

    public Puerta(String color) {
        if (color == null) {
            throw new IllegalArgumentException("El color no puede ser nulo");
        }
        this.color = color;
        estado = EstadoPuerta.CERRADA;
    }

    public String color() {
        return color;
    }

    public Puerta poner(Llave llave) {
        this.llave = llave;
        return this;
    }

    public Llave quitar() {
        Llave ret = llave;
        llave = null;
        return ret;
    }

    public boolean abrir() {
        if (estado == EstadoPuerta.ABIERTA) {
            return true;
        }
        if (llave != null && llave.color().equals(color)) {
            estado = EstadoPuerta.ABIERTA;
            return true;
        }
        return false;
    }

    public void cerrar() {
        estado = EstadoPuerta.CERRADA;
    }
}
