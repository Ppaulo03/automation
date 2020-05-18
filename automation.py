from selenium import webdriver


firefox_browser = webdriver.Firefox()

firefox_browser.maximize_window()
firefox_browser.get(
    'https://accounts.google.com/signup')
first_name = firefox_browser.find_element_by_id('firstName')
last_name = firefox_browser.find_element_by_id('lastName')
user_name = firefox_browser.find_element_by_id('username')

passoword = firefox_browser.find_element_by_name('Passwd')
confirm_pass = firefox_browser.find_element_by_name('ConfirmPasswd')

next_button = firefox_browser.find_element_by_id('accountDetailsNext')


first_name.clear()
last_name.clear()
user_name.clear()

passoword.clear()
confirm_pass.clear()

name = 'anyone'

first_name.send_keys("Someone")
last_name.send_keys("EveryOne")
user_name.send_keys(name)

passoword.send_keys("Any_thing123")
confirm_pass.send_keys("Any_thing123")

next_button.click()

while True:
    try:

        user_name.clear()
        possibilities = firefox_browser.find_elements_by_class_name('uBOgn')
        name = possibilities[0].get_attribute('data-username')
        user_name.send_keys(name)
        next_button.click()

    except Exception:
        break

print(name)


firefox_browser.close()
firefox_browser.quit()
