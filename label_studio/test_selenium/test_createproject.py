from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import allure



class TestCreateProject():
    @pytest.fixture()
    def test_setup(self):
        global driver
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = webdriver.Chrome(executable_path="D:/Cong cu va Moi truong phat trien phan mem/chromedriver/chromdriver.exe")
        driver.implicitly_wait(15)
        driver.maximize_window
        driver.get("http://localhost:8080")
        # driver.get("http://labelstudio-env.eba-pbtrgnpm.us-east-1.elasticbeanstalk.com/")
        yield
        driver.close()
        driver.quit()
    
    @allure.description("Create a valid project by project name and description")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_create_valid_project(self, test_setup):
        email_data = "labelstudio09@gmail.com"
        password_data = "1234asdfASDF" 
        with allure.step("Sign in Label Studio"):
            email = driver.find_element(By.ID,'email')
            email.send_keys(email_data)
            password = driver.find_element(By.ID,'password')
            password.send_keys(password_data)                   
            login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
            login_button.click()
        create_button = driver.find_element(By.CLASS_NAME,"ls-button_look_primary")
        if create_button.text == "Create":
           create_button.click()
        
        with allure.step("Entering project name"):
            project_name = driver.find_element(By.ID, "project_name") 
            project_name.send_keys("Sample Project")
            
         
        with allure.step("Entering description project"):     
            project_description = driver.find_element(By.ID, "project_description") 
            project_description.send_keys("This a simple project")
        
        with allure.step("Click save"):     
            save_button = driver.find_element(By.CLASS_NAME, "ls-button_look_primary") 
            if save_button.text == "Save":
                save_button.click()
        
    @allure.description("Create a project with not fill any field")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_not_fill_field_project(self, test_setup):
        email_data = "labelstudio09@gmail.com"
        password_data = "1234asdfASDF" 
        with allure.step("Sign in Label Studio"):
            email = driver.find_element(By.ID,'email')
            email.send_keys(email_data)
            password = driver.find_element(By.ID,'password')
            password.send_keys(password_data)                   
            login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
            login_button.click()
        create_button = driver.find_element(By.CLASS_NAME,"ls-button_look_primary")
        if create_button.text == "Create":
           create_button.click()
        
        with allure.step("Click save"):     
            save_button = driver.find_element(By.CLASS_NAME, "ls-button_look_primary") 
            if save_button.text == "Save":
                save_button.click()
        
    