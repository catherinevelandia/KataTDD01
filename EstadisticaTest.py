from unittest import TestCase

from Estadistica import Estadistica

class EstadisticaTest(TestCase):
    def testCalcularEstadisticaSinElementos(self):
        self.assertEqual(Estadistica().calcularEstadistica(''), [0, 0, 0], 'Numero de elementos, minimo, maximo + cadena vacia')

    def testCalcularEstadisticaUnElemento(self):
        self.assertEqual(Estadistica().calcularEstadistica('8'), [1, 8, 8], 'Numero de elementos, minimo, maximo + un elemento (8)')

    def testCalcularEstadisticaDosElementos(self):
        self.assertEqual(Estadistica().calcularEstadistica('8,2'), [2, 2, 8], 'Numero de elementos, minimo, maximo + dos elementos (8,2)')

    def testCalcularEstadisticaVariosElementos(self):
        self.assertEqual(Estadistica().calcularEstadistica('8,2,3,7,9'), [5, 2], 'Numero de elementos, minimo + cinco elementos (8,2,3,7,9)')