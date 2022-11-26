from selenium import webdriver
from selenium.webdriver.common.by import By


firefox_browser = webdriver.Firefox()

def sign_up(name, i=0):
    first_name = firefox_browser.find_element('id', 'firstName')
    last_name = firefox_browser.find_element('id', 'lastName')
    user_name = firefox_browser.find_element('id', 'username')

    passoword = firefox_browser.find_element('name', 'Passwd')
    confirm_pass = firefox_browser.find_element('name', 'ConfirmPasswd')

    next_button = firefox_browser.find_element('id', 'accountDetailsNext')


    first_name.clear()
    last_name.clear()
    user_name.clear()

    passoword.clear()
    confirm_pass.clear()

    first_name.send_keys("Someone")
    last_name.send_keys("EveryOne")
    user_name.send_keys(name)

    passoword.send_keys("Any_thing123")
    confirm_pass.send_keys("Any_thing123")

    next_button.click()

    try:
        phone_number = firefox_browser.find_element('id', 'phoneNumberId')

    except Exception:
        suggested = firefox_browser.find_element(By.CLASS_NAME, 'oMzjQd').find_elements(By.TAG_NAME, "button")[0]
        print(suggested.text)
        suggested.click()
        next_button.click()
        phone_number = firefox_browser.find_element('id', 'phoneNumberId')
        

if __name__ == '__main__':
    firefox_browser.maximize_window()
    firefox_browser.get('https://accounts.google.com/signup')
    sign_up('anyone')
    