import unittest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from pages.Register import Register
import time
from common.logger import Log
from common import constant

class TestCase(Register, unittest.TestCase):
    logger = Log('TestCase').get_log()
    TC_P001 = False

    def access_page(self):
        self.visit_page_base(constant.PAGE_URL)
        self.click_button_login()
        self.click_button_register()
    
    @classmethod
    def change_TC_P001_success(cls):
        cls.TC_P001 = True

    def test_TC_P001(self):
        print('Test case TC-P001')
        self.visit_page_base(constant.PAGE_URL)
        self.click_button_login()
        self.click_button_register()
        assert 'registration' in self.driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
        self.change_TC_P001_success()
        print('Success')

    def test_TC_P003(self):
        print('Test case TC-P003')
        if not self.TC_P001:
            assert False, 'Test case TC-P001 not pass'
            return
        self.access_page()
        self.click_dropdown_locale()
        english_locale = self.driver.find_element('xpath', "//*[contains(text(), 'English')]").is_displayed()
        vietnamese_locale = self.driver.find_element('xpath', "//*[contains(text(), 'Vietnamese')]").is_displayed()
        assert english_locale and vietnamese_locale, 'not show locale'
        print('Success')

    def test_TC_P006(self):
        print('Test case TC-P006')
        if not self.TC_P001:
            assert False, 'Test case TC-P001 not pass'
            return
        self.access_page()
        self.switch_to_vietnamese()
        self.submit_form()
        assert 'Vui lòng nhập email.' in self.driver.page_source
        assert 'Vui lòng nhập mật khẩu.' in self.driver.page_source
        print('Success')

    def test_TC_P007(self):
        print('Test case TC-P007')
        if not self.TC_P001:
            assert False, 'Test case TC-P001 not pass'
            return
        self.access_page()
        self.input_firstname()
        self.input_lastname()
        self.input_email()
        self.input_password_and_confirm()
        self.input_phone()
        
        self.submit_form()
        self.find_element(('xpath', "//*[contains(text(), 'Bạn cần xác minh địa chỉ email của mình để kích hoạt tài khoản của mình.')]"))
        assert 'Bạn cần xác minh địa chỉ email của mình để kích hoạt tài khoản của mình.' in self.driver.page_source
        print('Success')
    

if __name__ == '__main__':
    unittest.main()