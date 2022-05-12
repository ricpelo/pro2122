package dinero;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Date;
import java.util.HashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;

import interfaces.Numerable;
import personas.Cliente;

public class Cuenta implements Numerable {
    private long numero;
    private Set<Cliente> titulares;
    private List<Movimiento> movimientos;
    private double saldo;

    public Cuenta(long numero, Collection<Cliente> titulares) {
        this.numero = numero;
        this.titulares = new HashSet<Cliente>(titulares);
    }

    public Cuenta(long numero) {
        this.numero = numero;
        titulares = new HashSet<Cliente>();
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

    // public Cuenta quitarTitular(int indice) {
    //     titulares.remove(indice);
    //     return this;
    // }

    public Cuenta quitarTitular(Cliente cli) {
        titulares.remove(cli);
        return this;
    }

    public List<Cliente> getTitulares() {
        return new ArrayList<Cliente>(titulares);
    }

    public void mostrarTitulares() {
        for (Cliente c : titulares) {
            System.out.println(c.getNombre());
        }
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

        for (Movimiento m : movimientos) {
            suma += m.getImporte();
        }

        saldo = suma;
    }
}
