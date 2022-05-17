import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class Asignatura {
    private String denominacion;
    private int numTrimestres;
    private Set<Alumno> alumnos;

    private Map<Alumno,Map<Integer,Float>> notas;

    public Asignatura(String denominacion, int numTrimestres) {
        this.denominacion = denominacion;
        this.numTrimestres = numTrimestres;
        alumnos = new TreeSet<>();
        notas = new HashMap<>();
    }

    public boolean matricular(Alumno alumno) {
        notas.put(alumno, new HashMap<>());
        return alumnos.add(alumno);
    }

    public void setNota(Alumno alumno, int trimestre, float nota) {
        comprobarMatriculaAlumno(alumno);
        comprobarTrimestre(trimestre);
        notas.get(alumno).put(trimestre, nota);
    }

    public Float media(Alumno alumno) {
        comprobarMatriculaAlumno(alumno);
        Map<Integer,Float> notasAlumno = notas.get(alumno);
        float suma = 0f;
        int numNotas = 0;

        for (Float nota : notasAlumno.values()) {
            suma += nota;
            numNotas++;
        }

        if (numNotas == 0) {
            return null;
        }

        return suma / numNotas;
    }

    public void imprimirNotas() {
        Map<Integer,Float> notasAlumno;

        for (Alumno a : notas.keySet()) {
            System.out.println(a.getNombre());
            notasAlumno = notas.get(a);

            for (Integer i : notasAlumno.keySet()) {
                System.out.println(String.format("En el trimestre %d ha sacado %f", i, notas.get(i)));
            }
        }
    }

    public Float nota(Alumno alumno, int trimestre) {
        comprobarTrimestre(trimestre);

        if (!alumnos.contains(alumno)) {
            return null;
        }

        return notas.get(alumno).get(trimestre);
    }

    private void comprobarMatriculaAlumno(Alumno alumno) {
        if (!alumnos.contains(alumno)) {
            throw new IllegalArgumentException("El alumno no está matriculado de la asignatura");
        }
    }

    private void comprobarTrimestre(int trimestre) {
        if (trimestre < 0 || trimestre > numTrimestres) {
            throw new IllegalArgumentException("El trimestre no es correcto");
        }
    }
}
