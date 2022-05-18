import java.util.HashSet;
import java.util.List;

public class Principal {
    public static void main(String[] args) {
        Soporte soporte = new Soporte(List.of("Batman.mp4", "Superman.mp4"));

        assert (new Televisor()).encender().bajarVolumen().getVolumen() == 0;
        assert (new Televisor()).subirVolumen().encender().subirVolumen().getVolumen() == 1;
        assert (new Televisor()).conectar(soporte).reproducirSiConectado().equals(new HashSet<String>());
        assert (new Televisor()).conectar(soporte).encender().reproducirSiConectado().equals(new HashSet<String>(List.of("Batman.mp4", "Superman.mp4")));
    }
}
