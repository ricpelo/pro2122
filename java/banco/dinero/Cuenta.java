package dinero;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.List;
import java.util.Objects;
import interfaces.Numerable;
import personas.Cliente;

public class Cuenta implements Numerable {
    private long numero;
    private List titulares;
    private List movimientos;
    private double saldo;

    public Cuenta(long numero, Cliente[] titulares) {
        this.numero = numero;
        this.titulares = new ArrayList();

        for (Cliente c : titulares) {
            this.titulares.add(c);
        }
    }

    public Cuenta(long numero) {
        this.numero = numero;
        titulares = new ArrayList();
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }

        if (obj == null) {
            return false;
        }

        if (getClass() != obj.getClass()) {
            return false;
        }

        Cuenta otro = (Cuenta) obj;

        return Objects.equals(numero, otro.numero);
    }

    @Override
    public int hashCode() {
        return Objects.hash(numero);
    }

    public Cuenta insertarTitular(Cliente titular) {
        titulares.add(titular);
        return this;
    }

    public Cuenta quitarTitular(int indice) {
        titulares.remove(indice);
        return this;
    }

    public Cuenta quitarTitular(Cliente cli) {
        titulares.remove(cli);
        return this;
    }

    public List getTitulares() {
        ArrayList ar = (ArrayList) titulares;
        return (List) ar.clone();
    }

    public void mostrarTitulares() {
        Cliente c;

        for (Object o : titulares) {
            c = (Cliente) o;
            System.out.println(c.getNombre());
        }

        // for (int i = 0; i < titulares.size(); i++) {
        //     c = (Cliente) titulares.get(i);
        //     System.out.println(c.getNombre());
        // }
    }

    @Override
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
        movimientos.add(mov);
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

        Movimiento m;

        for (Object o : movimientos) {
            m = (Movimiento) o;
            suma += m.getImporte();
        }

        saldo = suma;
    }
}
