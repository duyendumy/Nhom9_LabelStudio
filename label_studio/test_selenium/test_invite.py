from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import allure
import constant

class TestInvite():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.implicitly_wait(15)
        driver.maximize_window
        # driver.get("http://localhost:8080")
        driver.get(constant.url)
        yield
        driver.close()
        driver.quit()
        
    @pytest.fixture()   
    def test_login(self, test_setup):
        email_data = "labelstudio09@gmail.com"
        password_data = "1234asdfASDF"
        with allure.step("Entering a valid email " + email_data):
            email = driver.find_element(By.ID,'email')
            email.send_keys(email_data)
            
        with allure.step("Entering a valid password " + password_data):
            password = driver.find_element(By.ID,'password')
            password .send_keys("1234asdfASDF")
            
        login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        
    @allure.description("Get token to invite member")  
    @allure.severity(severity_level = "NORMAL")      
    def test_get_invite_link(self, test_login):
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
        with allure.step("Copy token"):
            link = token.get_attribute("value")
            print("Token: " + link)
            
    @allure.description("Reset token to invite member")  
    @allure.severity(severity_level = "NORMAL")  
    def test_reset_invite_link(self, test_login):
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