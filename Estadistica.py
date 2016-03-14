
class Estadistica:
    def calcularEstadistica(self, cadena):
        if cadena == '':
            return [0, 0, 0];

        elif "," in cadena:
            arreglo = cadena.split(",")
            min = int(arreglo[0])
            max = int(arreglo[0])

            for a in arreglo:
                if int(a) <= min:
                    min = int(a)
                if int(a) > max:
                    max = int(a)

            return [len(arreglo), min, max]

        else:
            return [1, int(cadena), int(cadena)];


