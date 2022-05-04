package personas;

public class Menor extends Cliente {
    private Cliente representante;

    public Cliente getRepresentante() {
        return representante;
    }

    public void setRepresentante(Cliente representante) {
        this.representante = representante;
    }
}
