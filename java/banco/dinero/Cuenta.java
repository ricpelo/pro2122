package dinero;

import java.util.Arrays;
import java.util.Date;

import personas.Cliente;

public class Cuenta {
    private long numero;
    private Cliente[] titulares;
    private Movimiento[] movimientos;
    private double saldo;

    public Cuenta(long numero, Cliente[] titulares) {
        this.numero = numero;
        this.titulares = titulares;
    }

    public long getNumero() {
        return numero;
    }

    public void setNumero(long numero) {
        this.numero = numero;
    }

    public void insertarMovimiento(Date fecha, String concepto, double importe) {
        Movimiento mov = new Movimiento(fecha, concepto, importe);
        movimientos = Arrays.copyOf(
                movimientos,
                movimientos.length + 1);
        movimientos[movimientos.length - 1] = mov;
        saldo += mov.getImporte();
    }

    // public void insertar(Movimiento[] movs) {
    // int longAnterior = movimientos.length;

    // movimientos = Arrays.copyOf(
    // movimientos,
    // movimientos.length + movs.length
    // );

    // for (int i = 0; i < movs.length; i++) {
    // movimientos[longAnterior + i] = movs[i];
    // saldo += movs[i].getImporte();
    // }
    // }

    public void recalcularSaldo() {
        double suma = 0.0;

        for (int i = 0; i < movimientos.length; i++) {
            suma += movimientos[i].getImporte();
        }

        saldo = suma;
    }
}
