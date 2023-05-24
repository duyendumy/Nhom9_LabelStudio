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

class TestDeleteAnnotation():
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
        
    @allure.description("Delete an annotation")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_delete_annotation(self, test_setup):
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
            
        with allure.step("Choose Delete annotation"): 
            menus = driver.find_elements(By.CLASS_NAME,"lsf-annotation-button__contextMenu")
            menus[0].click()
            delete_annotation = driver.find_element(By.CLASS_NAME,"lsf-AnnotationButtonContextMenu__option_delete")
            delete_annotation.click()
        
        with allure.step("Click Delete button"):   
            delete_btn = driver.find_element(By.XPATH,'//button[contains(@class,"lsf-button lsf-button_size_compact lsf-button_look_destructive") and text()="Delete"]')
            delete_btn.click()
            
    @allure.description("Cancel delete an annotation")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_cancel_delete_annotation(self, test_setup):
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
            
        with allure.step("Choose Delete annotation"): 
            menus = driver.find_elements(By.CLASS_NAME,"lsf-annotation-button__contextMenu")
            menus[0].click()
            delete_annotation = driver.find_element(By.CLASS_NAME,"lsf-AnnotationButtonContextMenu__option_delete")
            delete_annotation.click()
        
        with allure.step("Click Cancel button"):   
            cancel_btn = driver.find_element(By.XPATH,'//button[contains(@class,"lsf-button lsf-button_size_compact lsf-button_look_") and text()="Cancel"]')
            cancel_btn.click()