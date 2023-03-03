from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

browser = webdriver.Chrome()

def open_website(link):
    browser.maximize_window()
    browser.get(link)

open_website("https://magento.softwaretestingboard.com/gear/bags.html")

input_box = WebDriverWait(browser, 30).until(EC.visibility_of_element_located(((By.XPATH, '//input[@name="q"]'))))
ActionChains(browser).move_to_element(input_box).click().perform()


ActionChains(browser).key_down(Keys.SHIFT).send_keys('a').key_up(Keys.SHIFT).send_keys('a').perform()

# gear_button1 = browser.find_element(By.XPATH, "//span[text()='Gear']")
# print(gear_button1)
#
# gear_button = browser.find_elements(By.XPATH, "//span[text()='Gear']")
# print(gear_button)

input_box.screenshot('foo.png')
# ActionChains(browser).move_to_element(gear_button).perform()


# open_website("https://www.google.com")

# input_box = browser.find_element(By.XPATH, '//input[@name="q"]')

# input_box.send_keys(Keys.ENTER)

# select_elem = browser.find_element(By.XPATH, '//select[@id="sorter"]')
# t = Select(select_elem)
# t.select_by_index(2)
#
# time.sleep(3)
# # select_elem = browser.find_element(By.XPATH, '//select[@id="sorter"]')
# t = Select(select_elem)
# t.select_by_index(1)
#
# time.sleep(3)
# # select_elem = browser.find_element(By.XPATH, '//select[@id="sorter"]')
# t = Select(select_elem)
# t.select_by_index(0)





