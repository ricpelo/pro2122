package personas;

public class Adulto extends Cliente {
    private Menor[] representados;

    public Adulto(String dni, String nombre) {
        super(dni, nombre);
        representados = new Menor[0];
    }

    public void anyadirRepresentado(Menor menor) {
        for (Menor m : representados) {
            if (m.equals(menor)) {
                return;
            }
        }
        int numElem = representados.length;
        Menor[] nuevos = new Menor[numElem + 1];
        System.arraycopy(representados, 0, nuevos, 0, numElem);
        nuevos[numElem] = menor;
        representados = nuevos;
    }
}
