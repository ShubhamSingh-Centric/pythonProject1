class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def go(self):
        self.browser.maximize_window()
        self.browser.get(self.url)


