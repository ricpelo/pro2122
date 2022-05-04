package pruebas;

public class Gato extends Animal {
    private String raza;

    public void mostrarNombre() {
        System.out.println(nombre);
    }

    public boolean iguales(Gato otro) {
        return raza.equals(otro.raza);
    }

    public boolean iguales(Animal otro) {
        return nombre.equals(otro.nombre);
    }
}
