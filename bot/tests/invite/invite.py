from selenium import webdriver
import os
import tests.constants as const
from selenium.webdriver.common.by import By
import time

class Invite(webdriver.Chrome):
    
    def __init__(self, driver_path=r"D:/Cong cu va Moi truong phat trien phan mem/chromedriver", teardown=True):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Invite, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
            print("Test Completed")
        
    def land_first_page(self):
        self.get(const.BASE_URL)
        
    def get_invite_link(self):
        email = self.find_element(By.ID,'email')
        # Send your email
        email.send_keys("labelstudio09@gmail.com")
        password = self.find_element(By.ID,'password')
        # Send your password
        password .send_keys("1234asdfASDF")
        login_button = self.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        
        hamburger = self.find_element(By.CLASS_NAME,'ls-hamburger_animated')
        hamburger.click()
        menu_item = self.find_elements(By.CLASS_NAME,'ls-main-menu__item')
        print(len(menu_item))
        for i in menu_item:
           if(i.text == "Organization"):
               i.click()
               break
        add_people_btn = self.find_element(By.CLASS_NAME,"ls-button_withIcon")
        add_people_btn.click()
        token = self.find_element(By.CLASS_NAME,"ls-input")
        link = token.get_attribute("value")
        print("Token: " + link)
    
    def reset_invite_link(self):
        email = self.find_element(By.ID,'email')
        # Send your email
        email.send_keys("labelstudio09@gmail.com")
        password = self.find_element(By.ID,'password')
        # Send your password
        password .send_keys("1234asdfASDF")
        login_button = self.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        
        hamburger = self.find_element(By.CLASS_NAME,'ls-hamburger_animated')
        hamburger.click()
        menu_item = self.find_elements(By.CLASS_NAME,'ls-main-menu__item')
        for i in menu_item:
           if(i.text == "Organization"):
               i.click()
               break
        add_people_btn = self.find_element(By.CLASS_NAME,"ls-button_withIcon")
        add_people_btn.click()
        reset_link_btn = self.find_element(By.CLASS_NAME,"ls-button_look_")
        reset_link_btn.click()
        token = self.find_element(By.CLASS_NAME,"ls-input")
        link = token.get_attribute("value")
        print("Reset token: " + link)
    

    
        
        
        
        
    
    