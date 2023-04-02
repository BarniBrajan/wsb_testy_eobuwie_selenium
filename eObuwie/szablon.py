import unittest


class RegistrationTest(unittest.TestCase):
    def setUp(self):
        ## warunki wstepne przed uruchomieniem testow
        """Przygotowanie testu"""
        print("przygotowanie")

    def tearDown(self):
        ## sprzatanie po tescie
        """Sprzatanie po tescie"""
        print("sprzątanie")
    
    def testNoNameEntered(self):
        """nazwa testu zaczyna sie od slowa - test"""
        print("test")

if __name__ == "__main__":
    unittest.main()



