import java.util.Scanner;

public class Prueba {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i, j;

        System.out.println("Introduzca dos números enteros:");

        while (!sc.hasNextInt()) {
            System.err.println("Se ha encontrado algo que no es un número");
            sc.next();
        }

        i = sc.nextInt();

        while (!sc.hasNextInt()) {
            System.err.println("Se ha encontrado algo que no es un número");
            sc.next();
        }

        j = sc.nextInt();

        System.out.println(i);
        System.out.println(j);
    }
}
