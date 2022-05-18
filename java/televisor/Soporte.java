import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class Soporte {
    private List<String> contenido;

    public Soporte(Collection<String> contenido) {
        this.contenido = new ArrayList<>(contenido);
    }

    public List<String> playlist() {
        return contenido;
    }

    public String reproducir(int indice) {
        return contenido.get(indice);
    }
}
