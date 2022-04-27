public class Ejemplo {
    public static void main(String[] args) {
        Prueba p = new Prueba();

        p.saludo("Ricardo");        // Correcto
        p.oculto();                 // Error: «oculto» es privado en «Prueba»
    }
}

class Prueba {
    public int x = 4;

    public void saludo(String nombre) {
        System.out.println("¡Hola, " + nombre + "!");
    }

    private void oculto() {
        System.out.println("No se puede llamar desde fuera de «Prueba»");
    }
}
