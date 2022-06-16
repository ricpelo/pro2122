import java.util.Arrays;

public class Ejercicio6 {
    public static void main(String[] args) {
        StringBuffer[] sb1 = new StringBuffer[] {
                new StringBuffer("A"),
                new StringBuffer("B"),
                new StringBuffer("C"),
                new StringBuffer("D"),
                new StringBuffer("E")
        };
        StringBuffer[] sb2 = Arrays.copyOf(sb1, sb1.length);
        sb1[0].append("AA");
        System.out.println(sb2[0]);
    }
}
