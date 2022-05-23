from pages.BasePage import BasePage
import random
import string

class Register(BasePage):
    login_button = ('xpath', "//*[contains(text(), 'Đăng nhập')]")
    register_button = ('css selector', "#kc-registration > span > a")
    locale_dropdown = ('id', 'kc-locale-dropdown')
    locale_vietnamese = ('xpath', "//a[contains(@href, 'vi')]")
    submit_button = ('css selector', "#kc-form-buttons > input[type='submit']")
    username_loc = ('id', 'username')
    firstname_loc = ('id', 'firstName')
    lastname_loc = ('id', 'lastName')
    email_loc = ('id', 'email')
    password_loc = ('id', 'password')
    password_confirm_loc = ('id', 'password-confirm')
    phone_loc = ('id', 'user.attributes.phone')
    PASSWORD = '12345678@a'

    def switch_to_frame(self, value):
        self.driver.switch_to.frame(value)

    def click_button_login(self):
        self.click_button(self.login_button)

    def click_button_register(self):
        self.click_button(self.register_button)

    def click_dropdown_locale(self):
        self.click_button(self.locale_dropdown)

    def input_username(self):
        self.click_button(self.username_loc)
        self.send_keys(self.username_loc, self.random_email())
    
    def switch_to_vietnamese(self):
        self.click_button(self.locale_dropdown)
        self.click_button(self.locale_vietnamese)

    def submit_form(self):
        self.click_button(self.submit_button)
    
    def random_email(self):
       random_char = ''.join(random.choice(string.ascii_lowercase) for _ in range(7))
       return random_char+"@gmail.com"

    def input_firstname(self):
        self.click_button(self.firstname_loc)
        self.send_keys(self.firstname_loc, self.random_email())

    def input_lastname(self):
        self.click_button(self.lastname_loc)
        self.send_keys(self.lastname_loc, self.random_email())
    
    def input_email(self):
        self.click_button(self.email_loc)
        self.send_keys(self.email_loc, self.random_email())

    def input_password(self):
        self.click_button(self.password_loc)
        self.send_keys(self.password_loc, self.PASSWORD)

    def input_password_and_confirm(self):
        self.click_button(self.password_loc)
        self.send_keys(self.password_loc, self.PASSWORD)
        self.click_button(self.password_confirm_loc)
        self.send_keys(self.password_confirm_loc, self.PASSWORD)

    def input_phone(self):
        self.click_button(self.phone_loc)
        self.send_keys(self.phone_loc, '0359431833')