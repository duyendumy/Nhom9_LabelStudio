from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import allure

class TestLogOut():
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
    
    @allure.description("Log out")  
    @allure.severity(severity_level = "NORMAL")      
    def test_logout(self, test_setup):
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
            
        avatar_button = driver.find_element(By.CLASS_NAME,'ls-userpic__username')
        avatar_button.click()
        
        with allure.step("Click Log Out"):
            menu_items = driver.find_elements(By.CLASS_NAME,"ls-main-menu__item")
            for item in menu_items:
                if item.text == "Log Out":
                    item.click()
                    break
      
