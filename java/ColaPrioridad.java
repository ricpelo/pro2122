public class ColaPrioridad extends Cola<Prioritario> {
    @Override
    public void meter(Prioritario elemento) {
        int prioridad = elemento.getPrioridad();

        for (int i = 0; i < elementos.size(); i++) {
            if (elementos.get(i).getPrioridad() > prioridad) {
                elementos.add(i, elemento);
                return;
            }
        }

        elementos.addLast(elemento);
    }
}
