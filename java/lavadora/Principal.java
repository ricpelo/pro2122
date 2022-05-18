public class Principal {
    public static void main(String[] args) {
        Lavadora lavadora = new Lavadora();
        lavadora.getDetergente().llenar(2.0f);
        lavadora.getSuavizante().llenar(1.0f);

        assert lavadora.cerrar().programar(3).encender().continuarPrograma().getPrograma() == 4;
        assert lavadora.cerrar().programar(3).encender().continuarPrograma().getDetergente().getRestante() - 1.6f < 0.00001f;
        assert lavadora.programar(3).encender().continuarPrograma().getPrograma() == 3;
        assert lavadora.cerrar().programar(3).continuarPrograma().getPrograma() == 3;
    }
}
