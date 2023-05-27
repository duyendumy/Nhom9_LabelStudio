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

class TestAnotherSortData():
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
        
     
            
        
    @allure.description("By Annotations")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_sort_data_by_annotations(self, test_sort_data):
        settings_button =  driver.find_element(By.XPATH, '//div[contains(@class,"dm-button-group dm-button-group_collapsed")]/button[contains(@class,"dm-button dm-button_size_medium dm-dropdown__trigger")]')
        settings_button.click()
        with allure.step("Choose Annotations"):
            order_by = driver.find_elements(By.CLASS_NAME,"dm-space_direction_horizontal")
            for item in order_by:
                print(item.text)
                if item.text == "Annotations":
                    item.click()
                    print("Choose Annotations")
                    break
                
    @allure.description("By Cancelled")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_sort_data_by_cancelled(self, test_sort_data):
        settings_button =  driver.find_element(By.XPATH, '//div[contains(@class,"dm-button-group dm-button-group_collapsed")]/button[contains(@class,"dm-button dm-button_size_medium dm-dropdown__trigger")]')
        settings_button.click()
        with allure.step("Choose Cancelled"):
            order_by = driver.find_elements(By.CLASS_NAME,"dm-space_direction_horizontal")
            for item in order_by:
                print(item.text)
                if item.text == "Cancelled":
                    item.click()
                    print("Choose Cancelled")
                    break
                
    @allure.description("By Predictions")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_sort_data_by_predictions(self, test_sort_data):
        settings_button =  driver.find_element(By.XPATH, '//div[contains(@class,"dm-button-group dm-button-group_collapsed")]/button[contains(@class,"dm-button dm-button_size_medium dm-dropdown__trigger")]')
        settings_button.click()
        with allure.step("Choose Predictions"):
            order_by = driver.find_elements(By.CLASS_NAME,"dm-space_direction_horizontal")
            for item in order_by:
                if item.text == "Predictions":
                    item.click()
                    print("Choose Predictions")
                    break
    
    allure.description("By Annotated by")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_sort_data_by_annotated_by(self, test_sort_data):
        settings_button =  driver.find_element(By.XPATH, '//div[contains(@class,"dm-button-group dm-button-group_collapsed")]/button[contains(@class,"dm-button dm-button_size_medium dm-dropdown__trigger")]')
        settings_button.click()
        with allure.step("Choose Annotated by"):
            order_by = driver.find_elements(By.CLASS_NAME,"dm-space_direction_horizontal")
            for item in order_by:
                if item.text == "Annotated by":
                    item.click()
                    print("Choose Annotated by")
                    break
                
    allure.description("By Prediction score")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_sort_data_by_prediction_score(self, test_sort_data):
        settings_button =  driver.find_element(By.XPATH, '//div[contains(@class,"dm-button-group dm-button-group_collapsed")]/button[contains(@class,"dm-button dm-button_size_medium dm-dropdown__trigger")]')
        settings_button.click()
        with allure.step("Choose Prediction score"):
            order_by = driver.find_elements(By.CLASS_NAME,"dm-space_direction_horizontal")
            for item in order_by:
                if item.text == "Prediction score":
                    item.click()
                    print("Choose Prediction score")
                    break
                
    @allure.description("By Prediction model versions")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_sort_data_by_prediction_model_versions(self, test_sort_data):
        settings_button =  driver.find_element(By.XPATH, '//div[contains(@class,"dm-button-group dm-button-group_collapsed")]/button[contains(@class,"dm-button dm-button_size_medium dm-dropdown__trigger")]')
        settings_button.click()
        with allure.step("Choose Prediction model versions"):
            order_by = driver.find_elements(By.CLASS_NAME,"dm-space_direction_horizontal")
            for item in order_by:
                if item.text == "Prediction model versions":
                    item.click()
                    print("Choose Prediction model versions")
                    break
                
    @allure.description("By Prediction Lead Time")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_sort_data_by_lead_times(self, test_sort_data):
        settings_button =  driver.find_element(By.XPATH, '//div[contains(@class,"dm-button-group dm-button-group_collapsed")]/button[contains(@class,"dm-button dm-button_size_medium dm-dropdown__trigger")]')
        settings_button.click()
        with allure.step("Choose Lead Time"):
            order_by = driver.find_elements(By.CLASS_NAME,"dm-space_direction_horizontal")
            for item in order_by:
                if item.text == "Lead Time":
                    item.click()
                    print("Choose Prediction Lead Time")
                    break
        
