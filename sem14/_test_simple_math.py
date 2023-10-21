import unittest

import simple_math


# https://docs.python.org/3/library/unittest.html#assert-methods
class TestSimpleMath(unittest.TestCase):
    def test_add(self):
        test_cases = [(4, 4), (10, 15), (-10, 10), (0.1, 0.2)]
        test_answers = [8, 25, 0, 0.3]

        for case, answer in zip(test_cases, test_answers):
            # self.assertEqual(simple_math.add(case[0], case[1]), answer)
            self.assertAlmostEqual(simple_math.add(case[0], case[1]), answer)

    def test_subtract(self):
        test_cases = [(4, 4), (10, 15), (-10, 10), (0.1, 0.2)]
        test_answers = [0, -5, -20, -0.1]

        for case, answer in zip(test_cases, test_answers):
            self.assertAlmostEqual(
                simple_math.subtract(case[0], case[1]), answer
            )


if __name__ == "__main__":
    unittest.main()
