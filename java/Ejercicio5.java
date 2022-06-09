import java.util.Arrays;
import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        int[] datos = new int[5];
        Scanner sc = new Scanner(System.in);
        int indice = 0;
        int dato;

        for (;;) {
            System.out.print("Introduzca el siguiente número: ");

            while (!sc.hasNextInt()) {
                sc.next();
            }

            dato = sc.nextInt();

            if (dato == 0) {
                break;
            }

            datos[indice++] = dato;

            if (indice >= datos.length) {
                datos = extenderArray(datos);
            }
        }

        for (int i = 0; i < indice; i++) {
            System.out.println(datos[i]);
        }
    }

    public static int[] extenderArray(int[] datos) {
        int lon = datos.length;
        return Arrays.copyOf(datos, lon + lon / 2);
    }
}
