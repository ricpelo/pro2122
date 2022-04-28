package dinero;

import java.util.Date;

public class Movimiento {
    private Date fecha;
    private String concepto;
    private double importe;

    public Movimiento(Date fecha, String concepto, double importe) {
        this.fecha = fecha;
        this.concepto = concepto;
        this.importe = importe;
    }

    public double getImporte() {
        return importe;
    }
}
