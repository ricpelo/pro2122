import java.util.Scanner;

public class Delimitadores {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in)
                .useDelimiter("\\s+");
        int i, j;

        i = sc.nextInt();
        j = sc.nextInt();
        System.out.println(i);
        System.out.println(j);
    }
}
