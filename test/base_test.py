import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--start-fullscreen")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.orioninc.com/")

    def closePage(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()
# test