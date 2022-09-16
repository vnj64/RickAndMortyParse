from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


DRIVER = webdriver.Chrome(executable_path="/home/sirius/parsers/all parsers/steamParse/chromedriver/chromedriver")


def steamParse(url):

    waitingTime = time.sleep(3)
    try:
        DRIVER.get(url=url)

        waitingTime
        
        search = DRIVER.find_element('id', 'store_nav_search_term')
        search.send_keys("action")
        search.send_keys(Keys.ENTER)
        
        waitingTime
        
        for_one_player = DRIVER.find_element('xpath', '//*[@id="TagFilter_Container"]/div[3]/span[1]/span/span[1]')
        for_one_player.click()
        
        waitingTime
        
        vr = DRIVER.find_element('xpath', '//*[@id="additional_search_options"]/div[8]/div[1]')
        vr.click()
        
        waitingTime
        
        button = DRIVER.find_element('xpath', '//*[@id="narrow_byVR"]/div[1]/span[1]/span/span[1]')
        button.click()
        
        waitingTime
        
        DRIVER.save_screenshot('scr1.png')
        DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        DRIVER.save_screenshot('scr2.png')
        
        waitingTime
        
        DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        DRIVER.save_screenshot('scr3.png')
        
        waitingTime
        
        DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        DRIVER.save_screenshot('scr4.png')
        
        waitingTime
        
        DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        DRIVER.save_screenshot('scr5.png')
        
        waitingTime
        
        DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        DRIVER.save_screenshot('scr6.png')
        
        waitingTime
        
        DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        DRIVER.save_screenshot('scr7.png')
        
        waitingTime
        
        DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        DRIVER.save_screenshot('scr8.png')
        
        waitingTime
        
        DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        DRIVER.save_screenshot('scr9.png')
        
        waitingTime

    except Exception as excep:
        print(excep)
        
    finally:
        DRIVER.close()
        DRIVER.quit()

steamParse("https://store.steampowered.com/")