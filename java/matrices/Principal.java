import java.util.List;

public class Principal {
    public static void main(String[] args) {
        Matriz una = new Matriz(List.of(2, 4, 9, 6, 5, 1, 3, 8, 7));
        Matriz otra = new Matriz(List.of(1, 1, 1, 2, 2, 2, 3, 3, 3));

        assert una.elem(1, 2) == 1;
        assert una.suma(otra).elem(2, 1) == 11;
        assert una.suma(new Matriz(List.of(1, 2, 3, 4))) == null;
    }
}
