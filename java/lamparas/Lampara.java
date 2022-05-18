import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// class Lampara:
//     def __init__(self, maximo_pequenyos, maximo_medianos, potencia_maxima):
//         self.__maximo = {PEQUENYO: maximo_pequenyos, MEDIANO: maximo_medianos}
//         self.__casquillos = {PEQUENYO: [], MEDIANO: []}
//         self.__potencia_maxima = potencia_maxima

//     def potencia_total(self):
//         return sum(x.potencia() for x in self.__casquillos[PEQUENYO] + self.__casquillos[MEDIANO])

//     def poner(self, bombilla):
//         if bombilla.potencia() + self.potencia_total() > self.__potencia_maxima:
//             return self
//         t = bombilla.tamanyo()
//         c = self.__casquillos[t]
//         if len(c) < self.__maximo[t]:
//             c.append(bombilla)
//         return self

//     def quitar(self, tamanyo):
//         c = self.__casquillos[tamanyo]
//         if len(c) == 0:
//             return None
//         return c.pop()

public class Lampara {
    private Map<Tamanyo, Integer> maximo;
    private Map<Tamanyo, List<Bombilla>> casquillos;
    private float potenciaMaxima;

    public Lampara(int maximoPequenyos, int maximoMedianos, float potenciaMaxima) {
        maximo = new HashMap<>();
        maximo.put(Tamanyo.PEQUENYO, maximoPequenyos);
        maximo.put(Tamanyo.MEDIANO, maximoMedianos);
        casquillos = new HashMap<>();
        casquillos.put(Tamanyo.PEQUENYO, new ArrayList<>());
        casquillos.put(Tamanyo.MEDIANO, new ArrayList<>());
        this.potenciaMaxima = potenciaMaxima;
    }

    public float potenciaTotal() {
        float suma = 0f;

        for (List<Bombilla> lista : casquillos.values()) {
            for (Bombilla b : lista) {
                suma += b.getPotencia();
            }
        }

        return suma;
    }

    public Lampara poner(Bombilla bombilla) {
        List<Bombilla> lista;
        Tamanyo tamanyo;

        if (bombilla.getPotencia() + potenciaTotal() > potenciaMaxima) {
            return this;
        }

        tamanyo = bombilla.getTamanyo();
        lista = casquillos.get(tamanyo);

        if (lista.size() < maximo.get(tamanyo)) {
            lista.add(bombilla);
        }

        return this;
    }

    public Bombilla quitar(Tamanyo tamanyo) {
        List<Bombilla> lista = casquillos.get(tamanyo);
        Bombilla bombilla;

        if (lista.size() == 0) {
            return null;
        }

        bombilla = lista.get(0);
        lista.remove(bombilla);
        return bombilla;
    }
}
