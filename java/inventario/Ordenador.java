import java.util.ArrayList;
import java.util.List;

public class Ordenador extends Inventariable implements IOrdenador {
    private IUbicacionOrdenador ubicacion;
    private List<IUbicacion> historico;

    public Ordenador(IUbicacionOrdenador ubicacion) {
        this.ubicacion = ubicacion;
        historico = new ArrayList<>();
        historico.add(ubicacion);
    }

    public IUbicacion ubicacion() {
        return ubicacion;
    }

    public IInventariable mover(IUbicacionOrdenador nuevaUbicacion) {
        ubicacion = nuevaUbicacion;
        historico.add(nuevaUbicacion);
        return this;
    }

    public List<IUbicacion> historico() {
        return new ArrayList<>(historico);
    }
}
