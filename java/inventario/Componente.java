import java.util.ArrayList;
import java.util.List;

public class Componente extends Inventariable {
    private String nombre;
    private IUbicacionComponente ubicacion;
    private List<IUbicacion> historico;

    public Componente(String nombre, IUbicacionComponente ubicacion) {
        this.nombre = nombre;
        this.ubicacion = ubicacion;
        historico = new ArrayList<>();
        historico.add(ubicacion);
    }

    public String getNombre() {
        return nombre;
    }

    public IUbicacionComponente ubicacion() {
        return ubicacion;
    }

    public IInventariable mover(IUbicacionComponente nuevaUbicacion) {
        ubicacion = nuevaUbicacion;
        historico.add(nuevaUbicacion);
        return this;
    }

    public List<IUbicacion> historico() {
        return new ArrayList<>(historico);
    }
}
