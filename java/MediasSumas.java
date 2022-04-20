import java.util.Scanner;

public class MediasSumas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] a;
        int n, cant_pos, cant_neg, suma;
        double media_pos, media_neg;

        for (;;) {
            System.out.print("Introduzca un número entero positivo (mayor que cero): ");

            while (!sc.hasNextInt()) {
                sc.next();
            }

            n = sc.nextInt();

            if (n <= 0) {
                System.err.println("El número introducido no es correcto.");
            } else {
                break;
            }
        }

        a = new int[n];

        for (int i = 0; i < a.length; i++) {
            System.out.print("Introduzca un número entero: ");

            while (!sc.hasNextInt()) {
                sc.next();
            }

            a[i] = sc.nextInt();
        }

        media_neg = media_pos = 0.0;
        cant_neg = cant_pos = suma = 0;

        for (int i = 0; i < a.length; i++) {
            if (a[i] < 0) {
                media_neg += a[i];
                cant_neg++;
            } else {
                media_pos += a[i];
                cant_pos++;
            }
            suma += a[i];
        }

        if (cant_neg == 0) {
            System.out.println("No hay media de negativos");
        } else {
            media_neg = media_neg / cant_neg;
            System.out.println("Media de negativos: " + media_neg);
        }

        if (cant_pos == 0) {
            System.out.println("No hay media de positivos");
        } else {
            media_pos = media_pos / cant_pos;
            System.out.println("Media de positivos: " + media_pos);
        }

        System.out.println("Suma total: " + suma);
    }
}
