import java.util.Collection;
import java.util.HashSet;

public class Alumno {
    private String nombre;
    private Collection<Asignatura> asignaturas;

    public Alumno(String nombre) {
        this.nombre = nombre;
        asignaturas = new HashSet<>();
    }

    public Alumno matricular(Asignatura asignatura) {
        asignaturas.add(asignatura);
        asignatura.anyadir(this);
        return this;
    }
}
