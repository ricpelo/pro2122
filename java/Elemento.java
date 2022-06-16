public class Elemento<E> implements Prioritario {
    private int prioridad;
    private E info;

    public Elemento(E info, int prioridad) {
        this.info = info;
        this.prioridad = prioridad;
    }

    public E getInfo() {
        return info;
    }

    @Override
    public int getPrioridad() {
        return prioridad;
    }
}
