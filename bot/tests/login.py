from selenium import webdriver
import os
import tests.constants as const
from selenium.webdriver.common.by import By
import time

class Login(webdriver.Chrome):
    def __init__(self, driver_path=r"D:/Cong cu va Moi truong phat trien phan mem/chromedriver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Login, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
        
    def land_first_page(self):
        self.get(const.BASE_URL)
    
    def login_by_valid_user(self):
        email = self.find_element(By.ID,'email')
        # Send your email
        email.send_keys("")
        password = self.find_element(By.ID,'password')
        # Send your password
        password .send_keys("")
        login_button = self.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        
    def login_by_incorrect_password(self):
        email = self.find_element(By.ID,'email')
        # Send your email
        email.send_keys("")
        password = self.find_element(By.ID,'password')
        # Send your incorrect password
        password .send_keys("")
        login_button = self.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
    
    def login_by_incorrect_email(self):
        email = self.find_element(By.ID,'email')
        # Send your incorrect email
        email.send_keys("")
        password = self.find_element(By.ID,'password')
        # Send your incorrect password
        password .send_keys("")
        login_button = self.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        
    def login_by_invalid_email(self):
        email = self.find_element(By.ID,'email')
        # Send your invalid email
        email.send_keys("invalidemail@gmail.com")
        password = self.find_element(By.ID,'password')
        # Send your invalid password
        password .send_keys("1234")
        login_button = self.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
    
    
  
        
     
            
        
        