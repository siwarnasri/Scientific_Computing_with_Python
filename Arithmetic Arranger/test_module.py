import unittest
from arithmetic_arranger import arithmetic_arranger


# the test case
class UnitTests(unittest.TestCase):
    def test_arrangement(self):
        print(" # Testing first arrangement without answers :")
        test_arrangement = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
        print(test_arrangement, '\n', '\n')
    
    def test_solutions(self):
        print(" # Testing first arrangement with answers :")
        test_solutions = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)
        print(test_solutions, '\n', '\n')

    def test_too_many_problems(self):
        print(" # Testing too many problems :")
        test_too_many_problems = arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
        print(test_too_many_problems, '\n', '\n')

    def test_incorrect_operator(self):
        print(" # Testing incorrect operator :")
        test_incorrect_operator = arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
        print(test_incorrect_operator, '\n', '\n')

    def test_too_many_digits(self):
        print(" # Testing too many digits :")
        test_too_many_digits = arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
        print(test_too_many_digits, '\n', '\n')

    def test_only_digits(self):
        print(" # Testing only digits :")
        test_only_digits = arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
        print(test_only_digits, '\n', '\n')


      

if __name__ == "__main__":
    unittest.main()