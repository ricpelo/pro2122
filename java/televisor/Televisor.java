import java.util.HashSet;
import java.util.Set;

public class Televisor {
    private boolean encendido;
    private int canal;
    private int volumen;
    private Soporte soporte;

    public Televisor() {
        encendido = false;
        canal = 1;
        volumen = 0;
        soporte = null;
    }

    public Televisor encender() {
        encendido = true;
        return this;
    }

    public Televisor apagar() {
        encendido = false;
        return this;
    }

    public Televisor subirVolumen() {
        if (encendido) {
            volumen = Math.min(volumen + 1, 30);
        }
        return this;
    }

    public Televisor bajarVolumen() {
        if (encendido) {
            volumen = Math.max(volumen - 1, 0);
        }
        return this;
    }

    public int getVolumen() {
        return volumen;
    }

    public Televisor sintonizar(int canal) {
        if (encendido && canal >= 1 && canal <= 100) {
            this.canal = canal;
        }
        return this;
    }

    public int getCanal() {
        return canal;
    }

    public Televisor conectar(Soporte soporte) {
        this.soporte = soporte;
        return this;
    }

    public Televisor desconectarSiConectado() {
        soporte = null;
        return this;
    }

    public Set<String> reproducirSiConectado() {
        if (encendido && soporte != null) {
            return new HashSet<>(soporte.playlist());
        }
        return new HashSet<>();
    }
}
