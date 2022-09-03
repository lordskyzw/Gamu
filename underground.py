from multiprocessing.dummy import freeze_support
from unicodedata import name
import undetected_chromedriver as uc 
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = uc.Chrome()
driver.get('https://instagram.com')
driver.find_element(By.NAME, 'username').send_keys('tarmicas_code')
driver.find_element(By.NAME, 'password').send_keys('Tarmica12580')
driver.find_element(By.TAG_NAME, 'form').submit()
sleep(60)   
driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()

if __name__ == '__main__':
                freeze_support()
