class BasePage:

    url = " "

    def __init__(self, browser):
        self.browser = browser


    def go(self):
        self.browser.maximize_window()
        self.browser.get(self.url)
