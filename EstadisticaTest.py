from unittest import TestCase

from Estadistica import Estadistica

class EstadisticaTest(TestCase):
    def testCalcularEstadisticaSinElementos(self):
        self.assertEqual(Estadistica().calcularEstadistica(''), [0,0], 'Numero de elementos, minimo + cadena vacia')

    def testCalcularEstadisticaUnElemento(self):
        self.assertEqual(Estadistica().calcularEstadistica('8'), [1], 'Numero de elementos + un elemento (8)')

    def testCalcularEstadisticaDosElementos(self):
        self.assertEqual(Estadistica().calcularEstadistica('8,2'), [2], 'Numero de elementos + dos elementos (8,2)')

    def testCalcularEstadisticaVariosElementos(self):
        self.assertEqual(Estadistica().calcularEstadistica('8,2,3,7,9'), [5], 'Numero de elementos + cinco elementos (8,2,3,7,9)')