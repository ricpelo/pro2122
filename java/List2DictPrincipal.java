import java.util.List;
import java.util.Map;

public class List2DictPrincipal {
    public static void main(String[] args) {
        List<Character> l = List.of('a', 'b', 'c');
        List<Boolean> y = List.of(true, false, true);

        Map<Integer, Character> m = List2Dict.list2dict(l);
        Map<Integer, Boolean> n = List2Dict.list2dict(y);

        for (Integer i : m.keySet()) {
            System.out.println(i + " => " + m.get(i));
        }
    }
}
