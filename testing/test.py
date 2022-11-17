# Linting is the first step: PEP8 etc...
# Built in module
import unittest
import main


class TestMain(unittest.TestCase):
    def test_do_something(self):
        test_param = 10
        result = main.do_something(test_param)
        self.assertEqual(result, 15)

    def test_do_something2(self):
        test_param = "SDfasd"
        result = main.do_something(test_param)
        self.assertIsInstance(result, TypeError)

    def test_do_something3(self):
        test_param = None
        result = main.do_something(test_param)
        self.assertEqual(result, main.please_enter_number)


unittest.main()
