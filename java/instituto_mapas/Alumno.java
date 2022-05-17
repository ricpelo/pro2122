import java.util.HashSet;
import java.util.Set;

public class Alumno implements Comparable<Alumno> {
    private String nombre;
    private Set<Asignatura> asignaturas;

    public Alumno(String nombre) {
        this.nombre = nombre;
        asignaturas = new HashSet<>();
    }

    public String getNombre() {
        return nombre;
    }

    public Alumno matricular(Asignatura asignatura) {
        asignaturas.add(asignatura);
        asignatura.matricular(this);
        return this;
    }

    @Override
    public int compareTo(Alumno o) {
        return nombre.compareTo(o.nombre);
    }

    public Alumno setNota(Asignatura asignatura, int trimestre, float nota) {
        asignatura.setNota(this, trimestre, nota);
        return this;
    }

    public Float media(Asignatura asignatura) {
        return asignatura.media(this);
    }

    public Float nota(Asignatura asignatura, int trimestre) {
        return asignatura.nota(this, trimestre);
    }

    public boolean aprobada(Asignatura asignatura) {
        Float m = media(asignatura);
        if (m == null) {
            return false;
        }
        return m >= 5.0f;
    }
}
