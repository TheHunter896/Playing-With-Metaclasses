from .as_dataframe import asDataframe
import unittest


class testWeirdDataframe(unittest.TestCase):

    def test_canDefineAttributesWithIndex(self):
        df = asDataframe()

        df[0] = [0, 1, 2, 3]
        df[1] = [1, 234, 5, 5]

        self.assertEqual(df['0'], [0, 1, 2, 3])
        self.assertEqual(df['1'], [1, 234, 5, 5])

    def test_canLoopOverAttributes(self):
        df = asDataframe()

        df[0] = [0,1,2,3]
        df[1] = [1,234,5,5]

        self.assertEqual([element for element in df], [df['0'], df['1']])

    def test_cannotDefineNoList(self):

        df = asDataframe()

        try:
            df[0] = [0]
        except Exception as err:
            self.assertEqual(isinstance(err, TypeError), True)


