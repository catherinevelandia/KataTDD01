
class Estadistica:
    def calcularEstadistica(self, cadena):
        if cadena == '':
            return [0, 0, 0, 0];

        elif "," in cadena:
            arreglo = cadena.split(",")
            min = int(arreglo[0])
            max = int(arreglo[0])
            total = 0;
            promedio = 0;

            for a in arreglo:
                total += int(a)
                if int(a) <= min:
                    min = int(a)
                if int(a) > max:
                    max = int(a)

            promedio = total / len(arreglo)
            return [len(arreglo), min, max, promedio]

        else:
            return [1, int(cadena), int(cadena), int(cadena)];


