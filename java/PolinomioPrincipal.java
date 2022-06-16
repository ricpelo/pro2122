import java.util.Arrays;

public class PolinomioPrincipal {
    public static void main(String[] args) {
        Polinomio p = new Polinomio(new int[] { 6, 2 });

        System.out.println(p.derivada());
    }
}

class Polinomio {
    private int[] coeficientes;

    public Polinomio(int[] coeficientes) {
        if (coeficientes.length == 0) {
            throw new IllegalArgumentException("Debe haber al menos un coeficiente");
        }
        this.coeficientes = coeficientes.clone();
    }

    public int grado() {
        return coeficientes.length - 1;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();

        if (grado() == 0 && coeficientes[0] == 0) {
            return "0";
        }

        for (int i = 0; i < coeficientes.length; i++) {
            if (i != 0 && coeficientes[i] > 0) {
                sb.append('+');
            }
            if (coeficientes[i] != 0) {
                sb.append(coeficientes[i]);
                if (i < grado()) {
                    sb.append('x');
                }
                if (i < grado() - 1) {
                    sb.append('^');
                    sb.append(grado() - i);
                }
            }
        }

        return sb.toString();
    }

    public Polinomio derivada() {
        int[] nuevosCoef;

        if (grado() == 0) {
            return new Polinomio(new int[] { 0 });
        }

        nuevosCoef = Arrays.copyOf(coeficientes, grado());

        for (int i = 0; i < nuevosCoef.length; i++) {
            nuevosCoef[i] *= grado() - i;
        }

        return new Polinomio(nuevosCoef);
    }
}
