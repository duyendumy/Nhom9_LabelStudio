from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import allure
import constant

class TestDeleteProject():
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
   
        
    @allure.description("Delete project")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_delete_project(self, test_login):
        list_project = driver.find_elements(By.CLASS_NAME, "ls-projects-page__link")
        list_project[0].click()
        
        with allure.step("Click Settings"):
            settings_button = driver.find_element(By.CLASS_NAME, "ls-button_look_")
            if settings_button.text == "Settings":
                settings_button.click()
        
        with allure.step("Click Danger Zone"):    
            list_main_menu_item = driver.find_elements(By.CLASS_NAME, "ls-main-menu__item")
            for item in list_main_menu_item:
                if item.text == "Danger Zone":
                    item.click()
                    break
        
        list_main_menu_button = driver.find_elements(By.CLASS_NAME, "ls-button_look_danger")
        for item in list_main_menu_button:
            driver.implicitly_wait(5)
            if item.text == "Delete Project":
                item.click()
                break
        
        with allure.step("Click Proceed"):  
            driver.implicitly_wait(5)
            if driver.find_element(By.CLASS_NAME, "ls-modal__body"):
                driver.implicitly_wait(15)
                list_button = driver.find_elements(By.CLASS_NAME, "ls-button")
                print(len(list_button))
                for button in list_button:
                    print(button.text)
                    if button.text == "Proceed":
                        button.click()
                        
    @allure.description("Cancel while deleting project")  
    @allure.severity(severity_level = "CRITICAL")         
    def test_cancel_delete_project(self, test_login):
        list_project = driver.find_elements(By.CLASS_NAME, "ls-projects-page__link")
        list_project[0].click()
        
        with allure.step("Click Settings"):
            settings_button = driver.find_element(By.CLASS_NAME, "ls-button_look_")
            if settings_button.text == "Settings":
                settings_button.click()
        
        with allure.step("Click Danger Zone"):    
            list_main_menu_item = driver.find_elements(By.CLASS_NAME, "ls-main-menu__item")
            for item in list_main_menu_item:
                if item.text == "Danger Zone":
                    item.click()
                    break
        
        list_main_menu_button = driver.find_elements(By.CLASS_NAME, "ls-button_look_danger")
        for item in list_main_menu_button:
            driver.implicitly_wait(5)
            if item.text == "Delete Project":
                item.click()
                break
        
        with allure.step("Click Cancel"):  
            driver.implicitly_wait(5)
            if driver.find_element(By.CLASS_NAME, "ls-modal__body"):
                driver.implicitly_wait(15)
                list_button = driver.find_elements(By.CLASS_NAME, "ls-button")
                print(len(list_button))
                for button in list_button:
                    print(button.text)
                    if button.text == "Cancel":
                        button.click()
                
                            
                            
            