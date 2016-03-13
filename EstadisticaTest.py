from unittest import TestCase

from Estadistica import Estadistica

class EstadisticaTest(TestCase):
    def test_calcularEstadistica(self):
        self.assertEqual(Estadistica().calcularEstadistica(''), [0], 'Numero de elementos + cadena vacia')
