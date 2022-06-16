import javax.sound.midi.MidiChannel;

public class PrincipalCola {
    public static void main(String[] args) {
        ColaPrioridad c = new ColaPrioridad();
        Elemento<String> e1 = new Elemento<>("uno", 1);
        Elemento<String> e3 = new Elemento<>("tres", 3);
        Elemento<String> e6 = new Elemento<>("seis", 6);

        c.meter(e6);
        c.meter(e1);
        c.meter(e3);

        while (!c.esVacia()) {
            Elemento e = (Elemento) c.sacar();
            System.out.println(e.getInfo());
        }
    }
}
