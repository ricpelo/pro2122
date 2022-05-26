import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class List2Dict {
    public static void main(String[] args) {
        List<Character> l = List.of('a', 'b', 'c');
        List<Boolean> y = List.of(true, false, true);

        Map<Integer, Character> m = list2dict(l);
        Map<Integer, Boolean> n = list2dict(y);

        for (Integer i : m.keySet()) {
            System.out.println(i + " => " + m.get(i));
        }
        // for (Integer i : n.keySet()) {
        //     System.out.println(i + " => " + n.get(i));
        // }
    }

    public static <E> Map<Integer, E> list2dict(List<E> lista) {
        Map<Integer, E> res = new LinkedHashMap<>();

        for (int i = 0; i < lista.size(); i++) {
            res.put(i, lista.get(i));
            res.put(i - lista.size(), lista.get(i));
        }

        return res;
    }
}
