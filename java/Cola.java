import java.util.LinkedList;

public class Cola<E> {
    protected LinkedList<E> elementos;

    public Cola() {
        elementos = new LinkedList<>();
    }

    public boolean esVacia() {
        return elementos.isEmpty();
    }

    public void meter(E elemento) {
        elementos.addLast(elemento);
    }

    public E sacar() {
        return elementos.removeFirst();
    }

    public E primero() {
        return elementos.getFirst();
    }

    public E ultimo() {
        return elementos.getLast();
    }
}
