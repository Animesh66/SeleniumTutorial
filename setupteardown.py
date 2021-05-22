import unittest


def setUpModule():
    print("This is setUpModule")  # this method will execute at the start of the module


def tearDownModule():
    print("This is tearDownModule")  # this method will execute at the end of the module

class AppTesting(unittest.TestCase):
    @classmethod # this is called decorator
    def setUp(self):  # setUp method will execute everytime before execution of each function
        print("I' set up method")

    @classmethod # this is called decorator
    def tearDown(self):  # tearDown method will execute everytime before execution of each function
        print("I'm tear down method")

    @classmethod
    def setUpClass(cls):  # this method will execute only one time before execution of other methods
        print("Set Up Class")

    @classmethod
    def tearDownClass(cls): # this method will execute only one time after execution of other methods
        print("Tear Down Class")

    def test_search(self):
        print("This is a search test")

    def test_advanced_search(self):
        print("This is a advanced search")

    def test_prepaid_recahrge(self):
        print("This is for prepaid recharge")

    def test_postpaid_recharge(self):
        print("This is a postpaid recharge")


if __name__ == "__main__":
    unittest.main()