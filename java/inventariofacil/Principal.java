import java.util.List;

public class Principal {
    public static void main(String[] args) {
        Aula p6 = new Aula("P6");
        Aula p7 = new Aula("P7");
        Armario armario = new Armario(p6);
        Ordenador comelta = new Ordenador(p6);
        Componente grafica = new Componente("Tarjeta gráfica", armario);
        Componente hdd = new Componente("Disco duro HDD", comelta);
        Componente ram = new Componente("8 GB de RAM", comelta);

        System.out.println(comelta.mover(p7).ubicacion() == p7);
        System.out.println(comelta.mover(p7).historico().equals(List.of(p6, p7)));
        System.out.println(hdd.ubicacion() == comelta);
        comelta.baja();
        System.out.println(hdd.ubicacion() == null);
    }
}
