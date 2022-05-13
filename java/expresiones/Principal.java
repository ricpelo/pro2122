public class Principal {
    public static void main(String[] args) {
        assert (new Numero(2)).valor() == 2;
        assert new Suma(new Numero(2),
                        new Producto(new Numero(3),
                                     new Numero(5))).valor() == 17;
        assert new Producto(new Numero(2),
                            new Suma(new Numero(3),
                                     new Numero(5))).valor() == 16;
    }
}
