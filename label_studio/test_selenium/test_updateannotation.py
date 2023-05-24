from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException, NoSuchElementException
import pytest
import allure
import constant

class TestUpdateAnnotation():
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
        
    @allure.description("Update an annotation")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_update_annotation(self, test_setup):
        email_data = "labelstudio09@gmail.com"
        password_data = "1234asdfASDF" 
        with allure.step("Sign in Label Studio"):
            email = driver.find_element(By.ID,'email')
            email.send_keys(email_data)
            password = driver.find_element(By.ID,'password')
            password.send_keys(password_data)                   
            login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
            login_button.click()
        list_project = driver.find_elements(By.CLASS_NAME, "ls-projects-page__link")
        list_project[0].click()
        
        with allure.step("Choose a task"):
            list_task = driver.find_elements(By.CLASS_NAME, "dm-table__row-wrapper")
            list_task[0].click()
        
        with allure.step("Choose an annotation"):
            list_annotation =  driver.find_elements(By.CLASS_NAME, "lsf-annotation-button")
            list_annotation[0].click()
            
        with allure.step("Click update button"):   
            update_btn = driver.find_element(By.XPATH,'//button[contains(@class,"lsf-button lsf-button_look_primary") and text()="Update"]')
            update_btn.click()
