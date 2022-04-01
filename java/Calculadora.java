import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double op1, op2, res = 0.0;
        String op;

        System.out.print("Introduzca el primer operando: ");
        while (!sc.hasNextDouble()) {
            sc.next();
            System.out.println("Entrada errónea.");
        }
        op1 = sc.nextDouble();

        System.out.print("Introduzca el segundo operando: ");
        while (!sc.hasNextDouble()) {
            sc.next();
            System.out.println("Entrada errónea.");
        }
        op2 = sc.nextDouble();

        System.out.print("Introduzca la operación: ");
        op = sc.next();

        boolean correcta = true;

        switch (op) {
            case "+":
                res = op1 + op2;
                break;

            case "-":
                res = op1 - op2;
                break;

            case "*":
                res = op1 * op2;
                break;

            case "/":
                res = op1 / op2;
                break;

            default:
                System.out.println("Operación incorrecta.");
                correcta = false;
                break;
        }

        if (correcta) {
            System.out.print("El resultado es: ");
            System.out.println(res);
        }

        sc.close();
    }
}
