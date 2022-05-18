public class Lavadora {
    private Deposito detergente;
    private Deposito suavizante;
    private boolean encendida;
    private int programa;
    private boolean abierta;

    public Lavadora() {
        detergente = new Deposito(3.0f);
        suavizante = new Deposito(5.0f);
        encendida = false;
        programa = 0;
        abierta = true;
    }

    public Deposito getDetergente() {
        return detergente;
    }

    public Deposito getSuavizante() {
        return suavizante;
    }

    public Lavadora encender() {
        if (!abierta && getDetergente().getRestante() >= 0.8f && getSuavizante().getRestante() >= 0.5f) {
            encendida = true;
        }
        return this;
    }

    public Lavadora apagar() {
        encendida = false;
        return this;
    }

    public  boolean getEncendida() {
        return encendida;
    }

    public int getPrograma() {
        return programa;
    }

    public Lavadora abrir() {
        if (!abierta && getPrograma() != 0) {
            abierta = true;
        }

        return this;
    }

    public Lavadora cerrar() {
        if (abierta) {
            abierta = false;
        }

        return this;
    }

    public Lavadora programar(int programa) {
        if (programa < 0 && programa > 4) {
            throw new IllegalArgumentException("Programa incorrecto");
        }

        if (!getEncendida()) {
            this.programa = programa;
        }

        return this;
    }

    public Lavadora continuarPrograma() {
        if (getPrograma() != 0 && getEncendida()) {
            programa += 1;
            if (programa == 5) {
                programa = 0;
                apagar();
            }
            getDetergente().quitar(0.4f);
            getSuavizante().quitar(0.4f);
        }

        return this;
    }
}
