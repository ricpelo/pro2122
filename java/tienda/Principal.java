import java.util.Map;

public class Principal {
    public static void main(String[] args) {
        Usuario usuario = new Usuario();
        Carrito carrito = usuario.getCarrito();
        Categoria tornilleria = new Categoria("Tornillería");
        Categoria ferreteria = new Categoria("Ferretería");
        Producto tuerca = new Producto(25, "Tuerca", 12.50, tornilleria);
        Producto grifo = new Producto(58, "Grifo", 6.30, ferreteria);
        carrito.anyadirProducto(tuerca);
        carrito.anyadirProducto(tuerca);
        Map<Producto, Integer> entradas = carrito.getEntradas();
        System.out.println(entradas.get(tuerca) == 2);
        System.out.println(entradas.get(grifo) == null);
        System.out.println(ferreteria.getProductos().contains(tuerca));
        System.out.println(ferreteria.getProductos().contains(grifo));
    }
}
