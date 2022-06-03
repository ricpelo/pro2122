public class Componente extends Inventariable {
    private String nombre;

    public Componente(String nombre, Ubicacion ubicacion) {
        super(ubicacion);
        this.nombre = nombre;
        setUbicacion(ubicacion);
    }

    public String getNombre() {
        return nombre;
    }

    protected void setUbicacion(Ubicacion ubicacion) {
        if (!(ubicacion instanceof Ordenador || ubicacion instanceof Armario)) {
            throw new IllegalArgumentException("Ubicación no válida.");
        }
        if (ubicacion instanceof Ordenador) {
            Ordenador o = (Ordenador) ubicacion;
            o.anyadirComponente(this);
        }
        this.ubicacion = ubicacion;
    }
}
