public class MSA {
    public static void main(String[] args) {
        int[] a;
        int cant_pos, cant_neg, suma;
        double media_pos, media_neg;

        if (args.length == 0) {
            System.out.println("Sintaxis: java MSA <número>+");
            return;
        }

        a = new int[args.length];

        for (int i = 0; i < a.length; i++) {
            a[i] = Integer.parseInt(args[i]);
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
