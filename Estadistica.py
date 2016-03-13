
class Estadistica:
    def calcularEstadistica(self, cadena):
        if cadena == '':
            return [0, 0];

        elif "," in cadena:
            arreglo = cadena.split(",")

            if len(arreglo) == 2:
                if arreglo[0] <= arreglo[1]:
                    return [len(arreglo), int(arreglo[0])]
                else:
                    return [len(arreglo), int(arreglo[1])]
            else:
                return [len(arreglo)]

        else:
            return [1, int(cadena)];


