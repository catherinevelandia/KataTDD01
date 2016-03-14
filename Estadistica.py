# Clase encargada de hacer los calculos estadisticos.
class Estadistica:

    # Funcion encargada de generar el arreglo dada una cadena
    # de enteros separados por comas con:
    # 1. Número de elementos [0]
    # 2. Mínimo [1]
    # 3. Máximo [2]
    # 4. Promedio [3]
    def calcularEstadistica(self, cadena):
        if cadena == '':
            return [0, 0, 0, 0]

        elif "," in cadena:
            arreglo = cadena.split(",")
            min = int(arreglo[0])
            max = int(arreglo[0])
            total = 0;

            for a in arreglo:
                total += int(a)
                if int(a) <= min:
                    min = int(a)
                if int(a) > max:
                    max = int(a)

            promedio = float(total) / len(arreglo)
            return [len(arreglo), min, max, promedio]

        else:
            return [1, int(cadena), int(cadena), int(cadena)]


