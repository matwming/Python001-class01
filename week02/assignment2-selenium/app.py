from selenium import webdriver
import time

# the demo email and password is listed below:
# email: tedigix813@frost2d.net
# password :753951

def is_login_success(browser) -> bool:
    new_doc_btn = browser.find_element_by_css_selector('.sm-button')
    if new_doc_btn.text == '新建':
        return True
    return False

def element_btns(browser):
    email = browser.find_element_by_name('mobileOrEmail')
    password = browser.find_element_by_name('password')
    login = browser.find_element_by_css_selector('.submit')
    return email, password, login

try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im/welcome')
    time.sleep(1)
    login_btn = browser.find_element_by_css_selector('.login-button')
    print(login_btn.text)
    if login_btn:
        login_btn.click()
        (input_email, input_password, login_btn) = element_btns(browser)
        input_email.send_keys('tedigix813@frost2d.net')
        input_password.send_keys('753951')
        time.sleep(1)
        login_btn.click()
        time.sleep(3)
        if is_login_success(browser):
            print('logged in shimo successfully!')
except:
    print('an error occurred.')
finally:
    print('chrome is closed')
    browser.quit()
