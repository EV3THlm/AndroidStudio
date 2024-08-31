package clases;

public class Usuario {
    private String nombre;
    private String nombreUsuario;
    private String password;

    public Usuario(String nombre, String nombreUsuario, String password){
        this.nombre = nombre;
        this.nombreUsuario = nombreUsuario;
        this.password = password;
    }

    /* _____________ GETTERS ___________*/
    public String getNombre() {
        return nombre;
    }

    public String getNombreUsuario(){
        return nombreUsuario;
    }

    public String getPassword(){
        return password;
    }

    /* _____________ SETTERS ___________*/
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setNombreUsuario(String nombreUsuario){
        this.nombreUsuario = nombreUsuario;
    }

    public void setPassword(String password){
        this.password = password;
    }

}
