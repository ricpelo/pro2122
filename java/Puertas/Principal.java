public class Principal {
    public static void main(String[] args) {
        assert (new Puerta("rojo")).poner(new Llave("rojo")).abrir() == true;
        assert (new Puerta("rojo")).poner(new Llave("verde")).abrir() == false;
        assert (new Puerta("rojo")).abrir() == false;
    }
}
