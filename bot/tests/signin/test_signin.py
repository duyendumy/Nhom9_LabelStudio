from selenium import webdriver
import os
import tests.constants as const
from selenium.webdriver.common.by import By
import time


class SignIn(webdriver.Chrome): 
    def setup_class(self, driver_path=r"D:/Cong cu va Moi truong phat trien phan mem/chromedriver", teardown=True):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(SignIn, self).setup_class()
        self.implicitly_wait(20)
        self.maximize_window()
        
    
    def teardown_class(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
            print("Test Completed")
        
    def test_land_first_page(self):
        self.get(const.BASE_URL)

        
    
    def test_login_by_valid_user(self):
        email = self.find_element(By.ID,'email')
        # Send your email
        email.send_keys("labelstudio09@gmail.com")
        password = self.find_element(By.ID,'password')
        # Send your password
        password .send_keys("1234asdfASDF")
        login_button = self.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        
    def login_by_incorrect_password(self):
        email = self.find_element(By.ID,'email')
        # Send your email
        email.send_keys("labelstudio09@gmail.com")
        password = self.find_element(By.ID,'password')
        # Send your incorrect password
        password .send_keys("incorrectpassword")
        login_button = self.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        error = self.find_element(By.CLASS_NAME,"error")
        text = error.text
        if text == "The email and password you entered don't match.":
            print("Pass")

    
    def login_by_incorrect_email(self):
        email = self.find_element(By.ID,'email')
        # Send your incorrect email
        email.send_keys("incorrectemail")
        password = self.find_element(By.ID,'password')
        # Send your incorrect password
        password .send_keys("1234asdfASDF")
        login_button = self.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        error = self.find_element(By.CLASS_NAME,"error")
        text = error.text
        if text == "The email and password you entered don't match.":
            print("Pass")
        
    def login_by_invalid_email(self):
        email = self.find_element(By.ID,'email')
        # Send your invalid email
        email.send_keys("invalidemail@gmail.com")
        password = self.find_element(By.ID,'password')
        # Send your invalid password
        password.send_keys("1234")
        login_button = self.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        error = self.find_element(By.CLASS_NAME,"error")
        text = error.text
        if text == "The email and password you entered don't match.":
            print("Pass")
    
    def not_fill_field_login(self):
        email = self.find_element(By.ID,'email')
        # Send your invalid email
        email.send_keys("")
        password = self.find_element(By.ID,'password')
        # Send your invalid password
        password.send_keys("")
        login_button = self.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        error = self.find_element(By.CLASS_NAME,"error")
        text = error.text
        if text == "The email and password you entered don't match.":
            print("Pass")
        
    
  
        
     
            
        
        