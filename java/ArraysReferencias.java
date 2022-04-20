public class ArraysReferencias {
    public static void main(String[] args) {
        String[] cadenas = new String[] { "hola", "pepe", "juan" };
        Object[] objetos = new Object[] { new Object(), new Object(), new Object() };

        objetos[2] = "hola";
    }
}
