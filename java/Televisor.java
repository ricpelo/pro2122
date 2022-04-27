public class Televisor {
    private int canal = 1;
    private int volumen = 0;
    private boolean encendido = false;
    private Pendrive multimedia;

    public int getCanal() {
        return canal;
    }

    public void setCanal(int canal) {
        if (canal >= 1 && canal <= 100) {
            this.canal = canal;
        }
    }

    public int getVolumen() {
        return volumen;
    }

    public void setVolumen(int volumen) {
        if (volumen >= 0 && volumen <= 30) {
            this.volumen = volumen;
        }
    }

    public boolean getEncendido() {
        return encendido;
    }

    private void setEncendido(boolean encendido) {
        this.encendido = encendido;
    }

    public void encender() {
        setEncendido(true);
    }

    public void apagar() {
        setEncendido(false);
    }


    public Pendrive getMultimedia() {
        return multimedia;
    }

    public void conectar(Pendrive multimedia) {
        this.multimedia = multimedia;
    }

    public void reproducir() {
        String[] contenido;

        if (this.getMultimedia() != null && this.getEncendido()) {
            contenido = multimedia.getContenido();

            for (int i = 0; i < contenido.length; i++) {
                System.out.println(contenido[i]);
            }
        }
    }
}

class Pendrive {
    private String[] contenido;

    public String[] getContenido() {
        return contenido;
    }

    public void setContenido(String[] contenido) {
        this.contenido = contenido;
    }
}
