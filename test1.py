from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

przegladarka = webdriver.Chrome()
przegladarka.get("https://www.google.com") 
przegladarka.maximize_window()
sleep(5)
przegladarka.find_element( by=By.XPATH, value='//*[@id="W0wltc"]/div' ).click()
serachField = przegladarka.find_element( by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input' )
serachField.send_keys("test")
serachField.send_keys(Keys.RETURN)

sleep(5)
