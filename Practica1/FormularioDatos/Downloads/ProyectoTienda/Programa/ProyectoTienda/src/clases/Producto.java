package clases;

public class Producto {
    public String codigoProducto;
    public String nombre;
    public float precio;

    public Producto(String codigoProducto, String nombre, float precio){
        this.codigoProducto = codigoProducto;
        this.nombre = nombre;
        this.precio = precio;
    }

    // ____________ GETTERS ___________

    public String getCodigoProducto(){
        return codigoProducto;
    }
    public String getNombre(){
        return nombre;
    }
    public float getPrecio(){
        return precio;
    }

    // ____________ SETTERS ___________
    public void setCodigoProducto(String codigoProducto){
        this.codigoProducto = codigoProducto;
    }
    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    public void setPrecio(float precio){
        this.precio = precio;
    }

    @Override
    public String toString(){
        return "\nProducto: "+nombre+
                "\nprecio: "+precio;
    }
}
