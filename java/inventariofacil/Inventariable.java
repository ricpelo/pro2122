import java.util.ArrayList;
import java.util.List;

public abstract class Inventariable {
    protected Ubicacion ubicacion;
    private List<Ubicacion> historico;

    abstract protected void setUbicacion(Ubicacion ubicacion);

    public Inventariable(Ubicacion ubicacion) {
        if (ubicacion == null) {
            throw new IllegalArgumentException("Falta la ubicación");
        }
        historico = new ArrayList<>();
        historico.add(ubicacion);
    }

    public Ubicacion ubicacion() {
        return ubicacion;
    }

    public List<Ubicacion> historico() {
        return new ArrayList<>(historico);
    }

    public Inventariable mover(Ubicacion nuevaUbicacion) {
        if (nuevaUbicacion == null) {
            throw new IllegalArgumentException("Está de baja y no se puede mover.");
        }
        setUbicacion(nuevaUbicacion);
        historico.add(nuevaUbicacion);
        return this;
    }

    public void baja() {
        ubicacion = null;
    }
}
