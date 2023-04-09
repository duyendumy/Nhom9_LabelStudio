from selenium import webdriver
import os
import tests.constants as const
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class SignUp(webdriver.Chrome):
    def __init__(self, driver_path=r"D:/Cong cu va Moi truong phat trien phan mem/chromedriver", teardown=True):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(SignUp, self).__init__()
        self.implicitly_wait(20)
        self.maximize_window()
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
            print("Test Completed")
            
    def land_first_page(self):
        self.get(const.BASE_URL)
    
    def signup_by_existing_account(self):
        signupLabels = WebDriverWait(self, timeout=20).until(lambda d: d.find_elements(By.TAG_NAME,"a"))
        signupLabels[0].click()
        email = self.find_element(By.ID,'email')
        # Send existing email
        email.send_keys("labelstudio09@gmail.com")
        password = self.find_element(By.ID,'password')
        # Send existing password
        password .send_keys("1234asdfASDF")
        signup_button = self.find_element(By.CLASS_NAME,'ls-button_look_primary')
        signup_button.click()
        self.implicitly_wait(60)
        # Check alert error
        if len(self.find_elements(By.CLASS_NAME, "field_errors")) != 0:
            print("Alert error 'User with this email already exists'")
    
    def not_fill_out_sign_up(self):
        signupLabels = WebDriverWait(self, timeout=20).until(lambda d: d.find_elements(By.TAG_NAME,"a"))
        signupLabels[0].click()
        email = self.find_element(By.ID,'email')
        email.send_keys("")
        password = self.find_element(By.ID,'password')
        password .send_keys("")
        signup_button = self.find_element(By.CLASS_NAME,'ls-button_look_primary')
        signup_button.click()
        self.implicitly_wait(60)
        # Check alert error
        if len(self.find_elements(By.CLASS_NAME, "field_errors")) == 2:
            print("Alert error 'Invalid email'")
            print("Alert error 'Please enter a password 8-12 characters in length'")

       
        
        
    
        
    