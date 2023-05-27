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

class TestSortData():
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
    @allure.description("Sort Data")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_sort_data(self, test_setup):
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
        
     
            
        
    @allure.description("By inner ID")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_sort_data_by_innerID(self, test_sort_data):
        settings_button =  driver.find_element(By.XPATH, '//div[contains(@class,"dm-button-group dm-button-group_collapsed")]/button[contains(@class,"dm-button dm-button_size_medium dm-dropdown__trigger")]')
        settings_button.click()
        with allure.step("Choose Inner ID"):
            order_by = driver.find_elements(By.CLASS_NAME,"dm-space_direction_horizontal")
            for item in order_by:
                print(item.text)
                if item.text == "Inner ID":
                    item.click()
                    print("Choose Inner ID")
                    break
                
    @allure.description("By Completed")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_sort_data_by_completed(self, test_sort_data):
        settings_button =  driver.find_element(By.XPATH, '//div[contains(@class,"dm-button-group dm-button-group_collapsed")]/button[contains(@class,"dm-button dm-button_size_medium dm-dropdown__trigger")]')
        settings_button.click()
        with allure.step("Choose Completed"):
            order_by = driver.find_elements(By.CLASS_NAME,"dm-space_direction_horizontal")
            for item in order_by:
                print(item.text)
                if item.text == "Completed":
                    item.click()
                    print("Choose Completed")
                    break
                
    @allure.description("By Annotation results")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_sort_data_by_annotation_results(self, test_sort_data):
        settings_button =  driver.find_element(By.XPATH, '//div[contains(@class,"dm-button-group dm-button-group_collapsed")]/button[contains(@class,"dm-button dm-button_size_medium dm-dropdown__trigger")]')
        settings_button.click()
        with allure.step("Choose Annotation results"):
            order_by = driver.find_elements(By.CLASS_NAME,"dm-space_direction_horizontal")
            for item in order_by:
                if item.text == "Annotation results":
                    item.click()
                    print("Choose Annotation results")
                    break
    
    allure.description("By Annotation IDs")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_sort_data_by_annotation_ids(self, test_sort_data):
        settings_button =  driver.find_element(By.XPATH, '//div[contains(@class,"dm-button-group dm-button-group_collapsed")]/button[contains(@class,"dm-button dm-button_size_medium dm-dropdown__trigger")]')
        settings_button.click()
        with allure.step("Choose Annotation IDs"):
            order_by = driver.find_elements(By.CLASS_NAME,"dm-space_direction_horizontal")
            for item in order_by:
                if item.text == "Annotation IDs":
                    item.click()
                    print("Choose Annotation IDs")
                    break
                
    allure.description("By Upload filename")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_sort_data_by_upload_filename(self, test_sort_data):
        settings_button =  driver.find_element(By.XPATH, '//div[contains(@class,"dm-button-group dm-button-group_collapsed")]/button[contains(@class,"dm-button dm-button_size_medium dm-dropdown__trigger")]')
        settings_button.click()
        with allure.step("Choose Upload filename"):
            order_by = driver.find_elements(By.CLASS_NAME,"dm-space_direction_horizontal")
            for item in order_by:
                if item.text == "Upload filename":
                    item.click()
                    print("Choose Upload filename")
                    break
                
    allure.description("By Storage filename")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_sort_data_by_storage_filename(self, test_sort_data):
        settings_button =  driver.find_element(By.XPATH, '//div[contains(@class,"dm-button-group dm-button-group_collapsed")]/button[contains(@class,"dm-button dm-button_size_medium dm-dropdown__trigger")]')
        settings_button.click()
        with allure.step("Choose Storage filename"):
            order_by = driver.find_elements(By.CLASS_NAME,"dm-space_direction_horizontal")
            for item in order_by:
                if item.text == "Storage filename":
                    item.click()
                    print("Choose Storage filename")
                    break
                
    @allure.description("By Updated at")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_sort_data_by_updated_at(self, test_sort_data):
        settings_button =  driver.find_element(By.XPATH, '//div[contains(@class,"dm-button-group dm-button-group_collapsed")]/button[contains(@class,"dm-button dm-button_size_medium dm-dropdown__trigger")]')
        settings_button.click()
        with allure.step("Choose Updated at"):
            order_by = driver.find_elements(By.CLASS_NAME,"dm-space_direction_horizontal")
            for item in order_by:
                if item.text == "Updated at":
                    item.click()
                    print("Choose Updated at")
                    break
                
    @allure.description("By Updated by")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_sort_data_by_updated_by(self, test_sort_data):
        settings_button =  driver.find_element(By.XPATH, '//div[contains(@class,"dm-button-group dm-button-group_collapsed")]/button[contains(@class,"dm-button dm-button_size_medium dm-dropdown__trigger")]')
        settings_button.click()
        with allure.step("Choose Updated by"):
            order_by = driver.find_elements(By.CLASS_NAME,"dm-space_direction_horizontal")
            for item in order_by:
                if item.text == "Updated by":
                    item.click()
                    print("Choose Updated by")
                    break
        
