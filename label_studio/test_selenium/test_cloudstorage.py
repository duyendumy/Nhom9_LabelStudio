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

class TestCloudStorage():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # driver = webdriver.Chrome(executable_path="D:/Cong cu va Moi truong phat trien phan mem/chromedriver/chromdriver.exe")
        driver.implicitly_wait(15)
        # driver.maximize_window
        driver.get("http://localhost:8080")
        # driver.get(constant.url)
        yield
        driver.close()
        driver.quit()
        
    @allure.description("Open Cloud Storage Of Project")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_open_cloud_storage(self, test_setup):
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
        
        with allure.step("Click Settings"):
            settings_button = driver.find_element(By.CLASS_NAME, "ls-button_look_")
            if settings_button.text == "Settings":
                settings_button.click()
        
        with allure.step("Click Cloud Storage"):    
            list_main_menu_item = driver.find_elements(By.CLASS_NAME, "ls-main-menu__item")
            for item in list_main_menu_item:
                if item.text == "Cloud Storage":
                    item.click()
                    break
    
    @allure.description("Add Storage Storage")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_add_source_storage(self, test_setup):
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
        
        with allure.step("Click Settings"):
            settings_button = driver.find_element(By.CLASS_NAME, "ls-button_look_")
            if settings_button.text == "Settings":
                settings_button.click()
        
        with allure.step("Click Cloud Storage"):    
            list_main_menu_item = driver.find_elements(By.CLASS_NAME, "ls-main-menu__item")
            for item in list_main_menu_item:
                if item.text == "Cloud Storage":
                    item.click()
                    break
        with allure.step("Click Add Source Storage"):
            add_source_btn = driver.find_element(By.XPATH,'//button[contains(@class,"ls-button ls-button_look_") and text()="Add Source Storage"]')
            add_source_btn.click()
        
        with allure.step("Select Local Files"):
            storage_type = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME,"storage_type")))
            storage_type.click()
            
            local_file = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//select/option[contains(@value, "localfiles")]')))
            local_file.click()
            
        with allure.step("Enter title and path"):
            input_title = self.find_element(By.NAME,'title').send_keys("Title")
            input_path = self.find_element(By.NAME,'path').send_keys("D:\Cong cu va Moi truong phat trien phan mem\DataSet\dataset1")
            input_regex_filter = self.find_element(By.NAME,'regex_filter').send_keys(".*")
            
            add_storage_btn = driver.find_element(By.XPATH, '//button[contains(@class,"ls-button_look_primary") and text()="Add Storage"]')
            add_storage_btn.click()
    
    @allure.description("Add Target Storage")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_add_target_storage(self, test_setup):
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
        
        with allure.step("Click Settings"):
            settings_button = driver.find_element(By.CLASS_NAME, "ls-button_look_")
            if settings_button.text == "Settings":
                settings_button.click()
        
        with allure.step("Click Cloud Storage"):    
            list_main_menu_item = driver.find_elements(By.CLASS_NAME, "ls-main-menu__item")
            for item in list_main_menu_item:
                if item.text == "Cloud Storage":
                    item.click()
                    break
        with allure.step("Click Add Target Storage"):
            add_source_btn = driver.find_element(By.XPATH,'//button[contains(@class,"ls-button ls-button_look_") and text()="Add Source Storage"]')
            add_source_btn.click()
        
        with allure.step("Select Local Files"):
            storage_type = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME,"storage_type")))
            storage_type.click()
            
            local_file = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//select/option[contains(@value, "localfiles")]')))
            local_file.click()
            
        with allure.step("Enter title and path"):
            input_title = self.find_element(By.NAME,'title').send_keys("Title")
            input_path = self.find_element(By.NAME,'path').send_keys("D:\Cong cu va Moi truong phat trien phan mem\DataSet\dataset1")
            input_regex_filter = self.find_element(By.NAME,'regex_filter').send_keys(".*")
            
            add_storage_btn = driver.find_element(By.XPATH, '//button[contains(@class,"ls-button_look_primary") and text()="Add Storage"]')
            add_storage_btn.click()
    
    @allure.description("Delete Target Storage")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_delete_source_storage(self, test_setup):
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
        
        with allure.step("Click Settings"):
            settings_button = driver.find_element(By.CLASS_NAME, "ls-button_look_")
            if settings_button.text == "Settings":
                settings_button.click()
        
        with allure.step("Click Cloud Storage"):    
            list_main_menu_item = driver.find_elements(By.CLASS_NAME, "ls-main-menu__item")
            for item in list_main_menu_item:
                if item.text == "Cloud Storage":
                    item.click()
                    break
        with allure.step("Click Delete Cloud Storage"):    
            try:
                settings_button =  driver.find_element(By.XPATH, '//div[contains(@class,"ls-card__header-extra")]/button[contains(@class,"ls-button_withIcon")]')
                settings_button.click()
                delete_span = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//select/option[contains(@class, "ls-main-menu__item") and text()="Delete"]')))
                delete_span.click()
                confirm_btn = driver.find_element(By.XPATH, '//button[contains(@class, "ls-button_look_destructive") and text()="OK"]')
                confirm_btn.click()
            except NoSuchElementException:
                return
            
    @allure.description("Cancel Delete Target Storage")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_delete_source_storage(self, test_setup):
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
        
        with allure.step("Click Settings"):
            settings_button = driver.find_element(By.CLASS_NAME, "ls-button_look_")
            if settings_button.text == "Settings":
                settings_button.click()
        
        with allure.step("Click Cloud Storage"):    
            list_main_menu_item = driver.find_elements(By.CLASS_NAME, "ls-main-menu__item")
            for item in list_main_menu_item:
                if item.text == "Cloud Storage":
                    item.click()
                    break
        with allure.step("Click Cancel Delete Cloud Storage"):    
            try:
                settings_button =  driver.find_element(By.XPATH, '//div[contains(@class,"ls-card__header-extra")]/button[contains(@class,"ls-button_withIcon")]')
                settings_button.click()
                delete_span = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//select/option[contains(@class, "ls-main-menu__item") and text()="Delete"]')))
                delete_span.click()
                confirm_btn = driver.find_element(By.XPATH, '//button[contains(@class, "ls-button_look_destructive") and text()="Cancel"]')
                confirm_btn.click()
            except NoSuchElementException:
                return
        
        
    
    