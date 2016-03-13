
class Estadistica:
    def calcularEstadistica(self, cadena):
        if cadena == '':
            return [0];
        elif "," in cadena:
            arreglo = cadena.split(",")
            return [len(arreglo)];
        else:
            return [1];


