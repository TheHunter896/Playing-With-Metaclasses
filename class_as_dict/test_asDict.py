import unittest
from .as_dict import asdict

class TestAsDict(unittest.TestCase):

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
        """
        Updates should update the attribute selected, can be sequential
        or non sequential (adapted from dict)
        :return:
        """

        ctest = asdict()

        ctest['test_1'] = 0
        ctest['test_2'] = 0

        #Sequential update
        ctest.update([('test_1', 1)])

        #Variable assignment test
        ctest.test_2 += 2

        #Non sequential test
        ctest['non_sequential'] = 0
        ctest.update(('non_sequential', 2))

        self.assertEqual(ctest.test_1, 1)
        self.assertEqual(ctest.test_2, 2)
        self.assertEqual(ctest.non_sequential, 2)

    def test_nongenericdefs(self):
        """
        Tests for variables of one instance being in the other
        Checks that there are no superclass variable definitions (all methods SHOULD be instance based)
        :return:
        """
        ctest = asdict()
        ctest_2 = asdict()

        ctest.test_1 = 0

        self.assertFalse('test_1' in ctest_2.__dict__.keys())

    def test_tostr(self):
        ctest = asdict()

        self.assertEqual(str(ctest), '{}', msg=ctest.__dict__.__str__())

    # Planned content
    def test_fromdict(self):
        ctest = asdict()

        test_dict = {
            'test_1': 'hi',
            'test_2': 2
        }

        ctest.fromdict(test_dict)

        self.assertEqual(ctest.test_1, 'hi')
        self.assertEqual(ctest.test_2, 2)

    def get(self):
        ctest = asdict()

        ctest.test_1 = 0
        ctest.test_2 = 0

        self.assertEqual(ctest.get(test_1), 0)
        self.assertEqual(ctest.get(test_2), 0)

    def test_popitem(self):
        ctest = asdict()

        ctest.test_1 = 0
        ctest.pop("test_1")

        self.assertFalse(ctest.get("test_1"))

    def test_items(self):
        ctest = asdict()

        ctest.test_1 = 0
        ctest['test_2'] = 0

        self.assertEqual(ctest.items(), {'test_1': 0, 'test_2': 0})

    def test_addDict(self):
        ctest = asdict()

        ctest.test_1 = 0
        ctest['test_1'] = 0

    def test_addClass(self):
        pass

    def test_subdict(self):
        pass

    def test_subclass(self):
        pass

    def test_multdict(self):
        pass

    def test_multclass(self):
        pass

    def test_gedict(self):
        pass

    def test_geclass(self):
        pass

    def test_ltdict(self):
        pass

    def test_gtclass(self):
        pass

    def test_joindict(self):
        pass

    def test_joinclass(self):
        pass

    def test_outerjoindict(self):
        pass

    def test_outerjoinclass(self):
        pass


if __name__ == '__main__':
    unittest.main()