import java.util.ArrayList;
import java.util.List;

public class Categoria {
    private String denominacion;
    private List<Producto> productos;

    public Categoria(String denominacion) {
        this.denominacion = denominacion;
        productos = new ArrayList<>();
    }

    public void anyadirProducto(Producto producto) {
        productos.add(producto);
    }

    public List<Producto> getProductos() {
        return new ArrayList<>(productos);
    }
}
