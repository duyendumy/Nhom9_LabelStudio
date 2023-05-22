from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import allure
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import constant


class TestInstruction():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.implicitly_wait(15)
        driver.maximize_window
        driver.get("http://localhost:8080")
        # driver.get(constant.url)
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
    
    @allure.description("Write Instruction")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_write_instruction(self, test_login):            
        with allure.step("Select project to write instruction"):
            list_project = driver.find_elements(By.CLASS_NAME, "ls-projects-page__link")
            list_project[0].click()
            
        with allure.step("Click Settings"):
            settings_button = driver.find_element(By.CLASS_NAME, "ls-button_look_")
            if settings_button.text == "Settings":
                settings_button.click()
        
        with allure.step("Click Instructions"):    
            list_main_menu_item = driver.find_elements(By.CLASS_NAME, "ls-main-menu__item")
            for item in list_main_menu_item:
                if item.text == "Instructions":
                    item.click()
                    break
        
        with allure.step("Write Instructions"): 
            expert_instruction = driver.find_element(By.NAME,"expert_instruction")
            expert_instruction.send_keys("Test instruction")
             
        with allure.step("Click Save"): 
            save_btn = driver.find_element(By.XPATH, '//button[contains(@type,"submit")]')
            save_btn.click