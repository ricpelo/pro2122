package personas;

public class Menor extends Cliente {
    private Adulto representante;

    public Menor(String dni, String nombre, Adulto representante) {
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

    public void setRepresentante(Adulto representante) {
        this.representante = representante;
        representante.anyadirRepresentado(this);
    }
}
