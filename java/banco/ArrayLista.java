public class ArrayLista<E> {
    private E[] elementos;

    public E get(int indice) {
        return elementos[indice];
    }

    public void set(int indice, E o) {
        elementos[indice] = o;
    }
}
