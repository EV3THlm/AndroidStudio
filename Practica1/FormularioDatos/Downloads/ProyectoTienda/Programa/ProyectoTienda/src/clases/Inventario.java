package clases;

public class Inventario {
    public Producto producto;
    public int stock;

    public Inventario(Producto producto, int stock){
        this.producto = producto;
        this.stock = stock;
    }

    public int getStock(){
        return stock;
    }

    public Producto getProducto(){
        return producto;
    }
}
