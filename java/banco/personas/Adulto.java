package personas;

import java.util.ArrayList;
import java.util.List;

public class Adulto extends Cliente {
    private List representados;

    public Adulto(String dni, String nombre) {
        super(dni, nombre);
        representados = new ArrayList();
    }

    public void anyadirRepresentado(Menor menor) {
        Menor m;

        if (representados.contains(menor)) {
            return;
        }

        representados.add(menor);
    }
}
