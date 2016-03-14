from unittest import TestCase
from Estadistica import Estadistica

class EstadisticaTest(TestCase):

    # Funcion encargada de probar el retorno del arreglo de estadisticas
    # para una cadena vacia.
    # Nota: se asumen todos los valores igual a 0
    def testCalcularEstadisticaSinElementos(self):
        self.assertEqual(Estadistica().calcularEstadistica(''), [0, 0, 0, 0], 'Numero de elementos, minimo, maximo, promedio + cadena vacia')

    # Función encargada de probar el retorno del arreglo de estadisticas
    # para una cadena con un solo numero.
    def testCalcularEstadisticaUnElemento(self):
        self.assertEqual(Estadistica().calcularEstadistica('8'), [1, 8, 8, 8], 'Numero de elementos, minimo, maximo, promedio + un elemento (8)')

    # Función encargada de probar el retorno del arreglo de estadisticas
    # para una cadena con dos numeros.
    def testCalcularEstadisticaDosElementos(self):
        self.assertEqual(Estadistica().calcularEstadistica('8,2'), [2, 2, 8, 5], 'Numero de elementos, minimo, maximo, promedio + dos elementos (8,2)')

    # Función encargada de probar el retorno del arreglo de estadisticas
    # para una cadena con varios numeros.
    def testCalcularEstadisticaVariosElementos(self):
        self.assertEqual(Estadistica().calcularEstadistica('8,2,3,7,9'), [5, 2, 9, 5.8], 'Numero de elementos, minimo, maximo + cinco elementos (8,2,3,7,9)')