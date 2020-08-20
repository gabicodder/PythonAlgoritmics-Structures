import unittest

def es_mayor_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaCristalTest(unittest.TestCase):
    
    def test_mayor_edad(self):
        edad = 20

        resultado = es_mayor_edad(edad)

        self.assertEqual(resultado,True)
    
    def test_menor_edad(self):
        edad =15

        resultado = es_mayor_edad(edad)

        self.assertEqual(resultado,False)



if __name__ == '__main__':
    unittest.main()