import unittest
from utilities import usefulMethods
from time import sleep

from selenium.webdriver.common.by import By


class RegistrationTest(unittest.TestCase):
    def setUp(self):
        ## warunki wstepne przed uruchomieniem testow
        """Przygotowanie testu"""
        self.handler = usefulMethods()
        self.handler.open_web()


    def tearDown(self):
        ## sprzatanie po tescie
        """Sprzatanie po tescie"""
        sleep(5)
        
    
    def testNoNameEntered(self):
        """nazwa testu zaczyna sie od slowa - test"""
        self.handler.open_registration_form()
        self.handler.fill_registration_form()
        self.handler.run_assertions()
        sleep(3)

if __name__ == "__main__":
    unittest.main()



