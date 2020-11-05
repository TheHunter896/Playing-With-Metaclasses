import unittest
from .transform import asdict

class TestAsDictMethods(unittest.TestCase):

    def test_lattributes(self):
        ctest = asdict()
        
        self.assertEqual(ctest.lattributes(), list(ctest.__dict__.keys()))

        ctest['test_1'] = 0
        self.assertEqual(ctest.lattributes(), ['test_1'])

        ctest.test_2 = 0
        self.assertEqual(ctest.lattributes(), ['test_1', 'test_2'])

    def test_assignment(self):
        ctest = asdict()

        ctest['test_1'] = 0
        ctest.test_2 = 0

        self.assertEqual(ctest['test_1'], 0)
        self.assertEqual(ctest['test_2'], 0)
        self.assertEqual(ctest.test_1, 0)
        self.assertEqual(ctest.test_2, 0)

    def test_lvalues(self):
        ctest = asdict()

        ctest['test_1'] = 0
        ctest.test_2 = 0

        self.assertEqual(ctest.lvalues(), [0,0])

    def test_update(self):
        ctest = asdict()

        ctest['test_1'] = 0
        ctest.update([('test_1', 1)])
        self.assertEqual(ctest.test_1, 1)


if __name__ == '__main__':
    unittest.main()