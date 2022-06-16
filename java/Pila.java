import java.util.LinkedList;

public class Pila<E> {
    private LinkedList<E> elementos;

    public Pila() {
        elementos = new LinkedList<>();
    }

    public boolean esVacia() {
        return elementos.isEmpty();
    }

    public void meter(E elemento) {
        elementos.push(elemento);
    }

    public E sacar() {
        return elementos.pop();
    }

    public E cima() {
        return elementos.getFirst();
    }
}
