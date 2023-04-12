from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest

class TestInvite():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="D:/Cong cu va Moi truong phat trien phan mem/chromedriver/chromdriver.exe")
        driver.implicitly_wait(15)
        driver.maximize_window
        driver.get("http://localhost:8080")
        yield
        driver.close()
        driver.quit()
        
    def test_get_invite_link(self, test_setup):
        email = driver.find_element(By.ID,'email')
        # Send your email
        email.send_keys("labelstudio09@gmail.com")
        password = driver.find_element(By.ID,'password')
        # Send your password
        password .send_keys("1234asdfASDF")
        login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        
        hamburger = driver.find_element(By.CLASS_NAME,'ls-hamburger_animated')
        hamburger.click()
        menu_item = driver.find_elements(By.CLASS_NAME,'ls-main-menu__item')
        print(len(menu_item))
        for i in menu_item:
           if(i.text == "Organization"):
               i.click()
               break
        add_people_btn = driver.find_element(By.CLASS_NAME,"ls-button_withIcon")
        add_people_btn.click()
        token = driver.find_element(By.CLASS_NAME,"ls-input")
        link = token.get_attribute("value")
        print("Token: " + link)
    
    def test_reset_invite_link(self, test_setup):
        email = driver.find_element(By.ID,'email')
        # Send your email
        email.send_keys("labelstudio09@gmail.com")
        password = driver.find_element(By.ID,'password')
        # Send your password
        password.send_keys("1234asdfASDF")
        login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        
        hamburger = driver.find_element(By.CLASS_NAME,'ls-hamburger_animated')
        hamburger.click()
        menu_item = driver.find_elements(By.CLASS_NAME,'ls-main-menu__item')
        for i in menu_item:
           if(i.text == "Organization"):
               i.click()
               break
        add_people_btn = driver.find_element(By.CLASS_NAME,"ls-button_withIcon")
        add_people_btn.click()
        reset_link_btn = driver.find_element(By.CLASS_NAME,"ls-button_look_")
        reset_link_btn.click()
        token = driver.find_element(By.CLASS_NAME,"ls-input")
        link = token.get_attribute("value")
        print("Reset token: " + link)