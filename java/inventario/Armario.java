public class Armario implements IArmario {
    private Aula aula;

    public Armario(Aula aula) {
        this.aula = aula;
    }

    public Aula getAula() {
        return aula;
    }
}
