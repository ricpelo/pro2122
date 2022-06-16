import java.util.HashMap;
import java.util.Map;

public class Carrito {
    private Map<Producto, Integer> productos;

    public Carrito() {
        productos = new HashMap<>();
    }

    public Map<Producto, Integer> getEntradas() {
        return productos;
    }

    public void anyadirProducto(Producto producto) {
        if (productos.containsKey(producto)) {
            productos.put(producto, productos.get(producto) + 1);
        } else {
            productos.put(producto, 1);
        }
    }

    // private int cantidadProducto(Producto producto) {
    //     if (!productos.containsKey(producto)) {
    //         throw new IllegalArgumentException("Producto inexistente en el carrito");
    //     }

    //     return productos.get(producto);
    // }

    public void quitarProducto(Producto producto) {
        int cantidad;

        if (!productos.containsKey(producto)) {
            throw new IllegalArgumentException("Producto inexistente en el carrito");
        }

        cantidad = productos.get(producto);

        if (cantidad > 1) {
            productos.put(producto, cantidad - 1);
        } else {
            productos.remove(producto);
        }
    }
}
