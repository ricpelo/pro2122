public class Producto {
    private int codigo;
    private String denominacion;
    private double precio;
    private Categoria categoria;

    public Producto(
            int codigo,
            String denominacion,
            double precio,
            Categoria categoria
    ) {
        this.codigo = codigo;
        this.denominacion = denominacion;
        this.precio = precio;
        this.categoria = categoria;
        categoria.anyadirProducto(this);
    }
}
