import time
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import unittest
from selenium import webdriver

class BasePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def find_element(self, loc):
        try:
            WebDriverWait(self.driver, 15).until(lambda driver:driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print(loc)
            self.logger.error('%s can not get ' % (self, loc))

    def visit_page_base(self, loc):
        self.driver.get(loc)
        self.driver.add_cookie({"name": "KEYCLOAK_LOCALE", "value": "vi", "path": "/"})

    def click_button(self, loc):
        self.find_element(loc).click()

    def clear_key(self, loc):
        time.sleep(1)
        self.find_element(loc).clear()

    def send_keys(self, loc, value):
        self.clear_key(loc)
        self.find_element(loc).send_keys(value)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()