public class Principal {
    public static void main(String[] args) {
        assert (new Lampara(3, 0, 20)).poner(new Bombilla(10, Tamanyo.PEQUENYO)).potenciaTotal() == 10;
        assert (new Lampara(3, 0, 20)).poner(new Bombilla(10, Tamanyo.MEDIANO)).potenciaTotal() == 0;
        assert (new Lampara(3, 2, 20)).poner(new Bombilla(10, Tamanyo.PEQUENYO)).poner(new Bombilla(10, Tamanyo.MEDIANO)).quitar(Tamanyo.MEDIANO).getTamanyo() == Tamanyo.MEDIANO;
    }
}
