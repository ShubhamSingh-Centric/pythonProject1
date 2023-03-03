from Page.google_home import GoogleHome
from selenium import webdriver


browser = webdriver.Chrome()

page = GoogleHome(browser)
page.go()
page.sign_in_button().click_element()
page.email_input_box().get_element().send_keys("shubham.the.singh@gmail.com")
page.next_button().click_element()
text = page.heading_text_after_next().get_text()
print(text)

# def test_text():
#     # assert 2 == 2
#     assert page.my_text().get_text() == 'Use your Google Account'