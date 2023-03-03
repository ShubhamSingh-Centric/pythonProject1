from Page.google_home import GoogleHome
from selenium import webdriver

browser = webdriver.Chrome()

page = GoogleHome(browser)
page.go()
page.sign_in_button().click_element()
page.my_text()