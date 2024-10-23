def es_par(n):
    return n % 2 == 0

import unittest

class TestEsPar(unittest.TestCase):
    
    def test_es_par(self):
        self.assertTrue(es_par(4))  
        self.assertFalse(es_par(7))  
        self.assertTrue(es_par(0))  
        self.assertTrue(es_par(-2))  

if __name__ == '__main__':
    unittest.main()







