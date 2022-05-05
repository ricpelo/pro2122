package personas;

public class Menor extends Cliente {
    private Cliente representante;

    public Menor(String dni, String nombre, Cliente representante) {
        super(dni, nombre);
        setRepresentante(representante);
    }

    // public Menor(String dni, String nombre) {
    //     this(dni, nombre, null);
    // }

    @Override
    public String toString() {
        return super.toString() + " - Representante: " + representante.toString();
    }

    public Cliente getRepresentante() {
        return representante;
    }

    public void setRepresentante(Cliente representante) {
        this.representante = representante;
    }
}
