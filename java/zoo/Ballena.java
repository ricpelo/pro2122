public class Ballena implements CantorNadador {
    @Override
    public void nada() {
        System.out.println("Voy nadando...");
    }

    @Override
    public void canta() {
        System.out.println("Troloro troloro...");
        Cantor.decirHola();
    }
}
