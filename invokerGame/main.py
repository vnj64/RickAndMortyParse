from selenium import webdriver
import time



DRIVER = webdriver.Chrome(executable_path="/home/sirius/parsers/all parsers/invokerGame/chromedriver/chromedriver")


def click_invoker(url):
    try:
        DRIVER.get(url=url)

        survival_button = DRIVER.find_element('xpath', '//*[@id="GameMenu"]/div/table/tbody/tr[2]/td[1]/input')
        survival_button.click()

        without_record = DRIVER.find_element('xpath', '//*[@id="LoginNotification"]/div/table/tbody/tr/td[3]/a')
        without_record.click()

        start_game = DRIVER.find_element('xpath', '//*[@id="GameInterface"]/div[1]/nobr/table/tbody/tr/td/input')
        start_game.click()

        spell_quas = DRIVER.find_element('xpath', '//*[@id="GameInterface"]/div[2]/div[1]')
        spell_wex = DRIVER.find_element('xpath', '//*[@id="GameInterface"]/div[2]/div[2]')
        spell_exort = DRIVER.find_element('xpath', '//*[@id="GameInterface"]/div[2]/div[3]')
        spell_one = DRIVER.find_element('xpath', '//*[@id="GameInterface"]/div[2]/div[4]')
        spell_two = DRIVER.find_element('xpath', '//*[@id="GameInterface"]/div[2]/div[5]')
        spell_ready = DRIVER.find_element('xpath', '//*[@id="GameInterface"]/div[2]/div[6]')


        time.sleep(1)

        for i in range(50):
            cold_snap(spell_quas, spell_ready, spell_one)
            ghost_walk(spell_quas, spell_wex, spell_ready, spell_one)
            ice_wall(spell_quas, spell_exort, spell_ready, spell_one)
            emp(spell_wex, spell_ready, spell_one)
            tornado(spell_wex, spell_quas, spell_ready, spell_one)
            alacrity(spell_wex, spell_exort, spell_ready, spell_one)
            sun_strike(spell_exort, spell_ready, spell_one)
            forge_spirit(spell_exort, spell_quas, spell_ready, spell_one)
            chaos_meteor(spell_exort, spell_wex, spell_ready, spell_one)
            blast(spell_exort, spell_quas, spell_wex, spell_ready, spell_one)




    except Exception as e:
        print(e)

    finally:

        time.sleep(10)

        DRIVER.close()
        DRIVER.quit()

def cold_snap(spell_quas, spell_ready, spell_one):
    for i in range(3):
        spell_quas.click()
    spell_ready.click()
    spell_one.click()

def ghost_walk(spell_quas, spell_wex, spell_ready, spell_one):
    for i in range(2):
        spell_quas.click()
    spell_wex.click()
    spell_ready.click()
    spell_one.click()

def ice_wall(spell_quas, spell_exort, spell_ready, spell_one):
    for i in range(2):
        spell_quas.click()

    spell_exort.click()
    spell_ready.click()
    spell_one.click()

def emp(spell_wex, spell_ready, spell_one):
    for i in range(3):
        spell_wex.click()

    spell_ready.click()
    spell_one.click()

def tornado(spell_wex, spell_quas, spell_ready, spell_one):
    for i in range(2):
        spell_wex.click()

    spell_quas.click()
    spell_ready.click()
    spell_one.click()

def alacrity(spell_wex, spell_exort, spell_ready, spell_one):
    for i in range(2):
        spell_wex.click()

    spell_exort.click()
    spell_ready.click()
    spell_one.click()

def sun_strike(spell_exort, spell_ready, spell_one):
    for i in range(3):
        spell_exort.click()

    spell_ready.click()
    spell_one.click()

def forge_spirit(spell_exort, spell_quas, spell_ready, spell_one):
    for i in range(2):
        spell_exort.click()
    spell_quas.click()

    spell_ready.click()
    spell_one.click()

def chaos_meteor(spell_exort, spell_wex, spell_ready, spell_one):
    for i in range(2):
        spell_exort.click()

    spell_wex.click()
    spell_ready.click()
    spell_one.click()

def blast(spell_exort, spell_quas, spell_wex, spell_ready, spell_one):
    spell_quas.click()
    spell_wex.click()
    spell_exort.click()
    spell_ready.click()
    spell_one.click()



click_invoker('https://www.invokergame.com/')