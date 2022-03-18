/*
* ¡Hola, mundo!
*/
public class Principal {
    public static void main(String[] args) {
        int x = (int) (Math.random() * 100);

        System.out.print("La x vale: ");
        System.out.println(x);

        if (x == 10 || x == 20) {
            System.out.println("La x vale 10 ó 20");
        } else {
            System.out.println("La x NO vale 10 ni 20");
        }

        switch (x) {
            case 10:
            case 20:
                System.out.println("La x vale 10 ó 20");
                break;
            default:
                System.out.println("La x NO vale 10 ni 20");
                break;
        }

        // if (x % 2 == 0) {
        //     System.out.println("La x es par");
        // } else {
        //     System.out.println("La x es impar");
        // }

        // switch (x % 2) {
        //     case 0:
        //         System.out.println("La x es par");
        //         break;
        //     case 1:
        //         System.out.println("La x es impar");
        //         break;
        // }

        // switch (x) {
        //     case 3:
        //     case 4:
        //         System.out.println("La x vale 3 ó 4");
        //         System.out.println("Hasta luego");
        //         break;
        //     case 5:
        //         System.out.println("La x vale 5");
        //         System.out.println("Bye bye");
        //         break;
        //     default:
        //         System.out.println("La x tiene otro valor distinto");
        //         System.out.println("Hasta luego");
        //         break;
        // }

        /*
        if (x < 7) {
            System.out.println("La x es menor que 7");
        } else if (x == 7) {
            System.out.println("La x es igual a 7");
        } else if (x == 8) {
            System.out.println("La x es igual a 8");
        } else {
            System.out.println("La x es mayor que 8");
        }
        */
    }
}
