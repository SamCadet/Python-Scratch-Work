import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        # Create objects to test default and custom raise
        self.sam = Employee('Sam', 'C', 100000)

    def testGiveCustomRaise(self):
        self.sam.giveRaise(6000)
        self.assertEqual(self.sam.annualSalary, 100000)

    def testGiveDefaultRaise(self):
        self.sam.giveRaise()
        self.assertEqual(self.sam.annualSalary, 100000)


# if __name__ == '__main__':
unittest.main()
