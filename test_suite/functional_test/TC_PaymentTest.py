import unittest


class PaymentTest(unittest.TestCase):
    def test_paymentinDollar(self):
        print("Payment in Dollars")
        self.assertTrue(True, "Test case is failed")

    def test_paymentinRupees(self):
        print("Payment in Rupees")
        self.assertTrue(True, "Test case is failed")


if __name__ == "__main__":
    unittest.main()