from selenium import webdriver
from selenium.webdriver.common.by import By
import time

DRIVER = webdriver.Chrome(YOUR_PATH)

URL = 'https://www.invokergame.com/'


DRIVER.get(URL)

DRIVER.find_element(By.XPATH,"/html/body/form/div[3]/div[6]/div[2]/div[2]/div/table/tbody/tr[2]/td[1]/input").click()
steam_login = DRIVER.find_element('xpath', '//*[@id="LoginNotification"]/div/table/tbody/tr/td[3]/a')
steam_login.click()

time.sleep(15)


DRIVER.find_element(By.XPATH,"/html/body/form/div[3]/div[6]/div[2]/div[3]/div[1]/nobr/table/tbody/tr").click()





body = DRIVER.find_element(By.XPATH,"/html/body")
while True:
    body.send_keys("QQQRD")
    body.send_keys("QQWRD")
    body.send_keys("QQERD")
    body.send_keys("WWWRD")
    body.send_keys("WWERD")
    body.send_keys("WWQRD")
    body.send_keys("EEERD")
    body.send_keys("EEQRD")
    body.send_keys("EEWRD")
    body.send_keys("QWERD")
