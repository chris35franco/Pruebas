import unittest
import random
import string

def generar_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

class TestGenerarID(unittest.TestCase):
    
    def test_generar_id(self):
        id1 = generar_id()
        id2 = generar_id()
        
        self.assertEqual(len(id1), 8)
        
        self.assertTrue(id1.isalnum())
        
        self.assertNotEqual(id1, id2)
        
        self.assertTrue(any(char.isdigit() for char in id1))
        self.assertTrue(any(char.isalpha() for char in id1))

if __name__ == '__main__':
    unittest.main()








