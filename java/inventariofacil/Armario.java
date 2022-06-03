public class Armario implements Ubicacion {
    private Ubicacion ubicacion;

    public Armario(Aula ubicacion) {
        this.ubicacion = ubicacion;
    }

    public Ubicacion getUbicacion() {
        return ubicacion;
    }
}
