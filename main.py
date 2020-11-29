from selenium import webdriver
import time
import random
import string

def generate_string(n):
    letters = string.ascii_letters + string.digits
    result = ''.join([random.choice(letters) for i in range(n)])
    return result

driver = webdriver.Firefox()
driver.get('https://mail.protonmail.com/create/new?language=en')
time.sleep(3)
driver.switch_to.frame(1)
time.sleep(1)
login = generate_string(15)
driver.find_element_by_xpath('/html/body/div/div/div/div/input').send_keys(login)
time.sleep(1)
driver.switch_to.default_content()
time.sleep(1)
password = generate_string(15)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/form/div[1]/div[2]/div[1]/div/input').send_keys(password)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/form/div[1]/div[2]/div[2]/div/input').send_keys(password)
time.sleep(1)
driver.switch_to.frame(0)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/footer/button').click()