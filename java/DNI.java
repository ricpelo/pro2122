import java.util.Scanner;

public class DNI {
    public static void main(String[] args) {
        final String letras = "TRWAGMYFPDXBNJZSQVHLCKE";
        Scanner sc = new Scanner(System.in);
        String dni;
        char letra_introducida, letra_correcta;
        int numero;

        for (;;) {
            System.out.print("Introduzca el DNI: ");
            dni = sc.nextLine();
            if (dni.length() != 9) {
                System.out.println("El DNI debe tener exactamente 9 caracteres.");
            } else {
                break;
            }
        }

        numero = Integer.parseInt(dni.substring(0, 8));
        letra_introducida = dni.charAt(8);
        letra_correcta = letras.charAt(numero % 23);

        if (letra_introducida == letra_correcta) {
            System.out.println("El DNI es correcto.");
        } else {
            System.out.println("El DNI es incorrecto.");
            System.out.println("La letra correcta debería ser " + letra_correcta + ".");
        }
    }
}
