public class Wrapper {
    public static void main(String[] args) {
        Integer a;
        int b;

        b = 17;
        a = b; // Autoboxing, equivale a 'a = Integer.valueOf(b);'

        a = Integer.valueOf(5);
        b = a; // Autounboxing, equivale a 'b = a.intValue();'
    }
}
