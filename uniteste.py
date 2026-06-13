import unittest

from teste_unitario import somar, subtrair, multiplicar, dividir 

class TestOperacoes(unittest.TestCase):
    
    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(-2, -3), -5)
    
    def test_subtrair(self):
        self.assertEqual(subtrair(5, 3), 2)
        self.assertEqual(subtrair(-1, 1), -2)
        self.assertEqual(subtrair(0, 0), 0) 
        
    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 3), 6)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(0, 5), 0)     
    
    def test_dividir(self):
        self.assertEqual(dividir(6, 2), 3)
        self.assertEqual(dividir(-6, 3), -2)
        with self.assertRaises(ValueError): 
            dividir(1, 0)    
    
if __name__ == '__main__':
    unittest.main()
        
    