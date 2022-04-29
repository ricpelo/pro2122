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
        this.titulares = titulares.clone();
    }

    public Cuenta(long numero) {
        this.numero = numero;
        titulares = new Cliente[0];
    }

    public Cuenta insertarTitular(Cliente titular) {
        titulares = Arrays.copyOf(
                titulares,
                titulares.length + 1);
        titulares[titulares.length - 1] = titular;
        return this;
    }

    public Cuenta quitarTitular(int indice) {
        Cliente[] dest;

        if (indice < 0 || indice >= titulares.length) {
            throw new IndexOutOfBoundsException(
                    "El índice está fuera de los límites");
        }

        dest = new Cliente[titulares.length - 1];
        System.arraycopy(titulares, 0, dest, 0, indice);
        System.arraycopy(
                titulares,
                indice + 1,
                dest,
                indice,
                titulares.length - indice - 1);
        titulares = dest;

        return this;
    }

    public Cuenta quitarTitular(Cliente cli) {
        for (int i = 0; i < titulares.length; i++) {
            if (titulares[i] == cli) {
                quitarTitular(i);
                break;
            }
        }

        return this;
    }

    public Cliente[] getTitulares() {
        return titulares.clone();
    }

    public void mostrarTitulares() {
        for (int i = 0; i < titulares.length; i++) {
            System.out.println(titulares[i].getNombre());
        }
    }

    public long getNumero() {
        return numero;
    }

    public void setNumero(long numero) {
        this.numero = numero;
    }

    public double getSaldo() {
        return saldo;
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

        // for (int i = 0; i < movimientos.length; i++) {
        //     suma += movimientos[i].getImporte();
        // }

        for (Movimiento m : movimientos) {
            suma += m.getImporte();
        }

        saldo = suma;
    }
}
