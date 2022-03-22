public class Bucles {
    public static void main(String[] args) {
        int total = 0;

        for (int i = 0; i < 10; i++) {
            if (i % 2 == 0) {
                continue;
            }
            total++;
        }

        // for (int i = 0; i < 10; i++) {
        //     for (int j = 0; j < 5; j++) {
        //         if (i + j > 10) {
        //             continue;
        //         }
        //         System.out.println(i + j);
        //         total++;
        //     }
        // }

        System.out.print("El total es: ");
        System.out.println(total);
    }
}
