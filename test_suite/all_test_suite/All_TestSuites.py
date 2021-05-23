import unittest
from test_suite.sanity_test.TC_LoginTest import LoginTest  # import all modules in the test suite
from test_suite.sanity_test.TC_SignupTest import SignupTest
from test_suite.functional_test.TC_PaymentTest import PaymentTest
from test_suite.functional_test.TC_PaymentReturnbyBank import PaymentReturnbyBank

# Get all test methods from LoginTest, SignupTest, PaymentTest, PaymentReturnbyBank

testcase_1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)   # this command will load all the test methods of LoginTest class
testcase_2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)  # this command will load all the test methods of SignupTest class
testcase_3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)  # this command will load all the test methods of PaymentTest class
testcase_4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnbyBank)  # this command will load all the test methods of PaymentReturnbyBank class

# Creating different test suites for test run

sanity_test_suite = unittest.TestSuite([testcase_1, testcase_2])  # this is sanity test suite
functional_test_suite = unittest.TestSuite([testcase_3, testcase_4])  # this is functional test suite
master_test_suite = unittest.TestSuite([testcase_1, testcase_2, testcase_3, testcase_4])  # this is master test suite


# Run a specific test suite

unittest.TextTestRunner().run(sanity_test_suite)  # run sanity test suite
