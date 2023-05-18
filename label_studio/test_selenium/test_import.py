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


class TestImportData():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       # driver = webdriver.Chrome(executable_path="D:/Cong cu va Moi truong phat trien phan mem/chromedriver/chromdriver.exe")
        driver.implicitly_wait(15)
        driver.maximize_window
        driver.get("http://localhost:8080")
        driver.get(constant.url)
        yield
        driver.close()
        driver.quit()
             
    
    @allure.description("Import data")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_import_dataset_url(self, test_setup):
        email_data = "labelstudio09@gmail.com"
        password_data = "1234asdfASDF" 
        with allure.step("Sign in Label Studio"):
            email = driver.find_element(By.ID,'email')
            email.send_keys(email_data)
            password = driver.find_element(By.ID,'password')
            password.send_keys(password_data)                   
            login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
            login_button.click()
            
        with allure.step("Select project to import"):
            list_project = driver.find_elements(By.CLASS_NAME, "ls-projects-page__link")
            list_project[0].click()
            
        with allure.step("Add URL"):
            import_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "dm-button_size_medium") and text()="Import"]')))    
            import_btn.click()
            # Upload URL
            driver.implicitly_wait(25)
            driver.find_element(By.NAME,"url").send_keys(r"https://firebasestorage.googleapis.com/v0/b/smartcloset-a6a3f.appspot.com/o/Android%20Images%2Fmsf%3A33?alt=media&token=11e9410b-d9da-411a-9800-5e3f01473a0c")
            submit_btn = driver.find_element(By.XPATH, '//button[contains(@type,"submit")]')
            submit_btn.click()
            time.sleep(100)
            
        with allure.step("Save data"):
            save_btn = driver.find_element(By.XPATH, '//button[contains(@class,"ls-button_look_primary") and text()="Import"]')
            save_btn.click()
        
    @allure.description("Import image")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_import_upload_image(self, test_setup):
        email_data = "labelstudio09@gmail.com"
        password_data = "1234asdfASDF" 
        with allure.step("Sign in Label Studio"):
            email = driver.find_element(By.ID,'email')
            email.send_keys(email_data)
            password = driver.find_element(By.ID,'password')
            password.send_keys(password_data)                   
            login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
            login_button.click()
            
        with allure.step("Select project to import"):
            list_project = driver.find_elements(By.CLASS_NAME, "ls-projects-page__link")
            list_project[0].click()
        
        cwd = os.getcwd()
        print(cwd)
        image_path = cwd + "/test_selenium/data_test/image1.png"
        with allure.step("Add file image"):
            import_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "dm-button_size_medium") and text()="Import"]')))    
            import_btn.click()
        
            input_upload = driver.find_element(By.ID, 'file-input')
            input_upload.send_keys(image_path)
            
        with allure.step("Save data"):
            save_btn = driver.find_element(By.XPATH, '//button[contains(@class,"ls-button_look_primary") and text()="Import"]')
            save_btn.click()    
        
    @allure.description("Import json")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_import_upload_json(self, test_setup):
        email_data = "labelstudio09@gmail.com"
        password_data = "1234asdfASDF" 
        with allure.step("Sign in Label Studio"):
            email = driver.find_element(By.ID,'email')
            email.send_keys(email_data)
            password = driver.find_element(By.ID,'password')
            password.send_keys(password_data)                   
            login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
            login_button.click()
            
        with allure.step("Select project to import"):
            list_project = driver.find_elements(By.CLASS_NAME, "ls-projects-page__link")
            list_project[0].click()
        
        cwd = os.getcwd()
        print(cwd)
        image_path = cwd + "/test_selenium/data_test/filejson1.json"
        with allure.step("Add file json"):
            import_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "dm-button_size_medium") and text()="Import"]')))    
            import_btn.click()
        
            input_upload = driver.find_element(By.ID, 'file-input')
            input_upload.send_keys(image_path)
            
        with allure.step("Save data"):
            save_btn = driver.find_element(By.XPATH, '//button[contains(@class,"ls-button_look_primary") and text()="Import"]')
            save_btn.click()    
    
    @allure.description("Import text")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_import_upload_text(self, test_setup):
        email_data = "labelstudio09@gmail.com"
        password_data = "1234asdfASDF" 
        with allure.step("Sign in Label Studio"):
            email = driver.find_element(By.ID,'email')
            email.send_keys(email_data)
            password = driver.find_element(By.ID,'password')
            password.send_keys(password_data)                   
            login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
            login_button.click()
            
        with allure.step("Select project to import"):
            list_project = driver.find_elements(By.CLASS_NAME, "ls-projects-page__link")
            list_project[0].click()
        
        cwd = os.getcwd()
        print(cwd)
        image_path = cwd + "/test_selenium/data_test/text1.txt"
        with allure.step("Add file text"):
            import_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "dm-button_size_medium") and text()="Import"]')))    
            import_btn.click()
        
            input_upload = driver.find_element(By.ID, 'file-input')
            input_upload.send_keys(image_path)
            
        with allure.step("Save data"):
            save_btn = driver.find_element(By.XPATH, '//button[contains(@class,"ls-button_look_primary") and text()="Import"]')
            save_btn.click()   
            
    @allure.description("Import video")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_import_upload_text(self, test_setup):
        email_data = "labelstudio09@gmail.com"
        password_data = "1234asdfASDF" 
        with allure.step("Sign in Label Studio"):
            email = driver.find_element(By.ID,'email')
            email.send_keys(email_data)
            password = driver.find_element(By.ID,'password')
            password.send_keys(password_data)                   
            login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
            login_button.click()
            
        with allure.step("Select project to import"):
            list_project = driver.find_elements(By.CLASS_NAME, "ls-projects-page__link")
            list_project[0].click()
        
        cwd = os.getcwd()
        print(cwd)
        image_path = cwd + "/test_selenium/data_test/video1.mp4"
        with allure.step("Add video"):
            import_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "dm-button_size_medium") and text()="Import"]')))    
            import_btn.click()
        
            input_upload = driver.find_element(By.ID, 'file-input')
            input_upload.send_keys(image_path)
            
        with allure.step("Save data"):
            save_btn = driver.find_element(By.XPATH, '//button[contains(@class,"ls-button_look_primary") and text()="Import"]')
            save_btn.click()   
       