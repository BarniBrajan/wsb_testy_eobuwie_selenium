import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with

class usefulMethods(unittest.TestCase):
    def open_web(self):
        self.chrome = webdriver.Chrome()
        self.chrome.get('https://www.eobuwie.pl')
        self.chrome.maximize_window()
        sleep(2)

    def open_registration_form(self):
        self.chrome.find_element(By.CSS_SELECTOR, value="button.e-button--type-primary.e-button--color-brand.e-consents-alert__button.e-button").click()
        sleep(3)
        self.chrome.find_element(By.XPATH, value='//a[@data-testid="header-register-link"]').click()

    def fill_registration_form(self):
        # 2. Wpisz nazwisko
        self.fill_field(fieldKey='lastname', value='Kowalski')
        # 3. Wpisz adres e-mail
        self.fill_field(fieldKey='email_address', value='Kowalski@abc.de' )
        # 4. Wpisz hasło (co najmniej 6 znaków)
        self.fill_field(fieldKey='password', value='Kowalski@abc.de' )
        # 5. Wpisz ponownie hasło w celu potwierdzenia
        self.fill_field(fieldKey='confirmation', value='Kowalski@abc.de' )
        # 6. Zaznacz „Oświadczam, że zapoznałem się z treścią Regulaminu serwisu i akceptuję jego postanowienia.”
        self.chrome.find_element(By.XPATH, '//label[@for="statement"]').click()
        # 7. Kliknij „Załóż nowe konto” (tylko dla przypadków niegatywnych!)
        self.chrome.find_element(By.ID, 'create-account').click()

    def fill_field(self, fieldKey, value):
        self.chrome.find_element(By.ID, fieldKey).send_keys(value)

    def run_assertions(self):
        spanErrors = self.chrome.find_elements(By.CLASS_NAME, 'form-error')
        self.assertEqual(1, len(spanErrors), "Powinien być jeden komunikat o błędzie!")
        self.assertEqual("To pole jest wymagane", spanErrors[0].text, "Niezgodna treśc komunikatu")
        
        name_not_entered_error_locator = locate_with(By.CLASS_NAME, "form-error").near({By.ID: "firstname"})
        name_not_entered_error = self.chrome.find_element(name_not_entered_error_locator)
        print(name_not_entered_error.id)
        print(spanErrors[0].id)
        self.assertEqual(name_not_entered_error.id, spanErrors[0].id)