import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class Matriz {
    private List<Integer> elementos;

    public Matriz(Collection<Integer> secuencia) {
        elementos = new ArrayList<>(secuencia);
    }

    public int getTamanyo() {
        return (int) Math.sqrt(elementos.size());
    }

    public Integer elem(int fila, int col) {
        return elementos.get(fila * getTamanyo() + col);
    }

    public Matriz suma(Matriz otra) {
        List<Integer> sec;

        if (getTamanyo() != otra.getTamanyo()) {
            return null;
        }

        sec = new ArrayList<>();

        for (int i = 0; i < getTamanyo(); i++) {
            for (int j = 0; j < getTamanyo(); j++) {
                sec.add(elem(i, j) + otra.elem(i, j));
            }
        }

        return new Matriz(sec);
    }
}
