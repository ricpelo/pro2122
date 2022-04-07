import java.util.Scanner;

public class Tabla {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int n;

        for (;;) {
            System.out.print("Introduzca el número (entre 0 y 10): ");

            while (!sc.hasNextInt()) {
                sc.next();
                System.err.println("Entrada incorrecta.");
                System.out.print("Introduzca el número (entre 0 y 10): ");
            }

            n = sc.nextInt();

            if (n < 0 || n > 10) {
                System.err.println("El número debe estar comprendido entre 0 y 10.");
            } else {
                break;
            }
        }

        for (int i = 0; i <= 10; i++) {
            // Opción 1:
            // System.out.print(n);
            // System.out.print(" x ");
            // System.out.print(i);
            // System.out.print(" = ");
            // System.out.println(n * i);
            // System.out.println(n + " x " + i + " = " + n * i);
            // Opción 2:
            // sb.append(n);
            // sb.append(" x ");
            // sb.append(i);
            // sb.append(" = ");
            // sb.append(n * i);
            // System.out.println(sb);
            // sb.delete(0, sb.length());
            // Opción 3:
            System.out.format("%d x %d = %d\n", n, i, n * i);
        }
    }
}
