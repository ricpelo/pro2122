public class Deposito {
    private float capacidad;
    private float restante;

    public Deposito(float capacidad) {
        this.capacidad = capacidad;
        restante = 0f;
    }

    public float getCapacidad() {
        return capacidad;
    }

    public float getRestante() {
        return restante;
    }

    public void llenar(float litros) {
        if (getRestante() + litros > getCapacidad()) {
            restante = getCapacidad();
        } else {
            restante += litros;
        }
    }

    public void quitar(float litros) {
        if (getRestante() - litros < 0f) {
            restante = 0f;
        } else {
            restante -= litros;
        }
    }

    public Deposito vaciar() {
        restante = 0;
        return this;
    }
}
