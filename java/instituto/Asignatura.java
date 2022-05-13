import java.util.Collection;
import java.util.HashSet;

public class Asignatura {
    private String denominacion;
    private int numTrimestres;
    private Collection<Alumno> alumnos;

    public Asignatura(String denominacion, int numTrimestres) {
        this.denominacion = denominacion;
        this.numTrimestres = numTrimestres;
        alumnos = new HashSet<>();
    }

    public boolean anyadir(Alumno alumno) {
        return alumnos.add(alumno);
    }
}
