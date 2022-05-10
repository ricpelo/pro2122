public interface Cantor {
    String cadena = "Soy un cantor"; // Variable estática final pública

    void canta(); // Método abstracto público

    private String cadena() {  // Método concreto privado
        return Cantor.cadena;
    }

    private static String hola() {  // Método estático privado
        return "Hola";
    }

    static void decirHola() { // Método estático público
        System.out.println(hola());
    }

    default void cantar() {  // Método concreto predeterminado público
        System.out.println(cadena());
    }
}
