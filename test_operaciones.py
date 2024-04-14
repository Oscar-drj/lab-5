import unittest
from operaciones import sumar, restar, mult, div

class TestOperaciones(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(3,2),5)
        self.assertEqual(sumar(-1,1),0)
        self.assertEqual(sumar(-1,-1),-2)

    def test_restar(self):
        self.assertEqual(restar(3,2),1)
        self.assertEqual(restar(-1,1),-2)
        self.assertEqual(restar(-4,-2),-2)
        self.assertEqual(restar(1,-1),2)

    def test_mult(self):
        self.assertEqual(mult(3,2),6)
        self.assertEqual(mult(-1,1),-1)
        self.assertEqual(mult(-1,-1),1)

    def test_div(self):
        self.assertEqual(div(4,2),2)
        self.assertEqual(div(-1,1),-1)
        self.assertEqual(div(-1,-1),1)
        self.assertEqual(div(0,4),0)


if __name__ == "__main__":
    unittest.main()