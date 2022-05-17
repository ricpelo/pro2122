public class Principal {
    public static void main(String[] args) {
        Asignatura ingles = new Asignatura("Inglés", 3);
        Asignatura mates = new Asignatura("Matemáticas", 2);

        Alumno juan = new Alumno("Juan Pérez");
        Alumno antonio = new Alumno("Antonio García");

        juan.matricular(ingles).matricular(mates);
        juan
            .setNota(ingles, 1, 4.0f)
            .setNota(ingles, 2, 6.0f)
            .setNota(ingles, 3, 8.0f);


        antonio.matricular(mates);
        antonio.setNota(mates, 1, 2.5f);

        // Tests:
        assert juan.media(ingles) == 6.0f;
        assert antonio.nota(mates, 2) == null;
        assert Math.abs(antonio.nota(mates, 1) - antonio.media(mates)) < 0.00001f;
        assert juan.aprobada(ingles) == true;
    }
}
