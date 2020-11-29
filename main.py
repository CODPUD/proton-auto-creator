from selenium import webdriver
import time
import random
import string

class ProtonMail():
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.set_preference('dom.webdriver.enabled', False)
        self.driver = webdriver.Firefox(options=options)
        self.driver.maximize_window()

    def generate_string(self, n):
        letters = string.ascii_letters + string.digits
        result = ''.join([random.choice(letters) for i in range(n)])
        return result

    def fillForm(self):
        self.driver.get('https://mail.protonmail.com/create/new?language=en')
        time.sleep(3)
        self.driver.switch_to.frame(1)
        time.sleep(1)
        login = self.generate_string(15)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/input').send_keys(login)
        time.sleep(1)
        self.driver.switch_to.default_content()
        time.sleep(1)
        password = self.generate_string(15)
        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/div[1]/form/div[1]/div[2]/div[1]/div/input').send_keys(password)
        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/div[1]/form/div[1]/div[2]/div[2]/div/input').send_keys(password)
        time.sleep(1)
        self.driver.switch_to.frame(0)
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div/div/footer/button').click()

    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    root = ProtonMail()
    root.fillForm()