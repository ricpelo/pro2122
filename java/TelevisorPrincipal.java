public class TelevisorPrincipal {
    public static void main(String[] args) {
        Televisor t = new Televisor();
        Pendrive p = new Pendrive();

        p.setContenido(new String[] { "Batman.mp4", "Superman.mp4" });

        t.setCanal(25);
        t.conectar(p);
        System.out.println(t.getCanal());

        t.encender();
        t.reproducir();
    }
}
