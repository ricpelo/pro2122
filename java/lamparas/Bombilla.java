public class Bombilla {
    private float potencia;
    private Tamanyo tamanyo;

    public Bombilla(float potencia, Tamanyo tamanyo) {
        // if (!List.of(Tamanyo.PEQUENYO, Tamanyo.MEDIANO).contains(tamanyo)) {
        //     throw new IllegalArgumentException("Tamaño incorrecto");
        // }
        this.potencia = potencia;
        this.tamanyo = tamanyo;
    }

    public float getPotencia() {
        return potencia;
    }

    public Tamanyo getTamanyo() {
        return tamanyo;
    }
}
