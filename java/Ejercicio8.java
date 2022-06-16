public class Ejercicio8 {
    public static void main(String[] args) {
        final int[] array = new int[] { 5, 6, 7, 8, 9 };
        cambiar(array);

        if (array[0] != 5) {
            System.out.println("Ha cambiado");
        } else {
            System.out.println("NO ha cambiado");
        }
    }

    private static void cambiar(final int[] ar) {
        ar[0] = 99;
    }
}
