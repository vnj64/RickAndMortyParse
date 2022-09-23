from lib2to3.pgen2 import driver
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


login = 'vnj64'
password = 'kamil200304'
anime_name = 'Токийский гуль'
comment = 'прелестное аниме, аж руки дрожат'

def main():

    driver = webdriver.Chrome(executable_path='/home/sirius/parsers/all parsers/yummyAnime/chromedriver/chromedriver')
    driver.get('https://yummyanime.org/')

    register = driver.find_element("xpath" ,'/html/body/div[1]/div/header/div[2]').click()

    sleep(1)
    
    log_in = driver.find_element("id" ,"login_name")
    log_in.send_keys(login)
    
    sleep(1)
    password_anime = driver.find_element("id" ,"login_password")
    password_anime.send_keys(password)
    
    sleep(1)
    driver.find_element('id', "login_not_save").click()
    
    sleep(1)
    enter = driver.find_element('xpath', '/html/body/div[2]/form/div[1]/div[3]/button').click()
    
    sleep(1)

    genres_button = driver.find_element('xpath', '/html/body/div[1]/div/header/div[3]').click()

    sleep(1)

    kiddy_genre = driver.find_element('xpath', '//*[@id="mobile-menu"]/div/ul/li[1]/ul/li[18]/a').click()

    sixth = driver.find_element('xpath', '//*[@id="pagination"]/div/a[5]').click()

    find_anime = driver.find_element('xpath', '//*[@id="dle-content"]/a[7]').click()

    comments = driver.find_element('xpath', '//*[@id="comments_ifr"]').click()

    sleep(6)

    send_button = driver.find_element('xpath', '//*[@id="add-comments-form"]/div[2]/div/button').click()




    driver.close()
    driver.quit()

if __name__ == '__main__':
    main()