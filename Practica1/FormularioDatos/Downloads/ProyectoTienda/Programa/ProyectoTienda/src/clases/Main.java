package clases;

import java.util.ArrayList;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        Administrador administrador1 = new Administrador("Ebeth", "EV3TH", "1234");
        Vendedor vendedor1 = new Vendedor("Alberto", "JOSA", "4321");

        // Instancia de productos
        Producto producto1 = new Producto("PRODUC1", "Smart TV", 8000);
        Producto producto2 = new Producto("PRODUC2", "PS4", 6000);

        Inventario inventario1 = new Inventario(producto1, 55);
        Inventario inventario2 = new Inventario(producto2, 10);

        // Lista de productos
        ArrayList<Inventario> inventario = new ArrayList<>();
        inventario.add(inventario1);
        inventario.add(inventario2);


        String codigoDeProductoAComprar = "PRODUC2";
        for (Inventario i: inventario){
            if (i.getProducto().getCodigoProducto().equals(codigoDeProductoAComprar)){
                System.out.println("¡Compra realizada con exito!");
                i.stock -= 1;
                break;
            }
        }

        for (Inventario i: inventario){
            System.out.println("Stock actual: "+i.getStock());
        }


        //System.out.println("\nNombre del administrador: "+administrador1.getNombre());
        //System.out.println("\nNombre del vendedor: "+vendedor1.getNombre());

        float sumaTotalProductos = 0;
        int opcion;
        do{
            System.out.println("\n1) Realizar compra");
            System.out.println("2) Ver stock");
            System.out.println("0) Salir");
            System.out.print("Ingresa tu opcion: ");
            opcion = teclado.nextInt();
            
            switch (opcion){
                case 1:
                    System.out.print("\nIngresa el codigo de producto: ");
                    String codigo = teclado.next();

                    for (Inventario i : inventario){
                        if(i.getProducto().getCodigoProducto().equals(codigo)){
                            System.out.println("\n"+i.getProducto());
                            i.stock -=1;
                            sumaTotalProductos += i.getProducto().getPrecio();
                            break;
                        }
                        else{
                            System.out.println("¡Codigo no reconocido, intenta nuevamente!");
                        }
                    }
                        break;
                case 2:
                    for (Inventario i : inventario){
                        System.out.println("\nStock actual: "+i.getProducto().nombre+" "+i.getStock());
                    }
                        break;
            }
        }while (opcion != 0);
        System.out.println("\nPrecio total a pagar: "+sumaTotalProductos);

    }
}
