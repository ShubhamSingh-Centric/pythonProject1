from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.google.com")

search_box = driver.find_element(By.XPATH, "//input[@name='q']")

search_box.send_keys("Car")
search_box.send_keys(Keys.ENTER)

image_tab = driver.find_element(By.XPATH, "//div[@class='hdtb-mitem']//a[text()='Images']")
image_tab.click()

import os

print(os)