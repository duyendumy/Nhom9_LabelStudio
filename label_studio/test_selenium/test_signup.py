from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import allure

class TestSingUp():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # driver = webdriver.Chrome(executable_path="D:/Cong cu va Moi truong phat trien phan mem/chromedriver/chromdriver.exe")
        driver.implicitly_wait(15)
        driver.maximize_window
        driver.get("http://localhost:8080")
        yield
        driver.close()
        driver.quit()
    
            
    
    @allure.description("Sign up Label Studio by existing account")  
    @allure.severity(severity_level = "NORMAL")  
    def test_signup_by_existing_account(self, test_setup):
        signupLabels = WebDriverWait(driver, timeout=20).until(lambda d: d.find_elements(By.TAG_NAME,"a"))
        signupLabels[0].click()
        email_data = "labelstudio09@gmail.com"
        password_data = "1234asdfASDF"
        with allure.step("Entering a existing email " + email_data):
            email = driver.find_element(By.ID,'email')
            email.send_keys("labelstudio09@gmail.com")
            
        with allure.step("Entering a existing password " + password_data):
            password = driver.find_element(By.ID,'password')
            password .send_keys("1234asdfASDF")
            
        signup_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
        signup_button.click()
        driver.implicitly_wait(60)
        # Check alert error
        if len(driver.find_elements(By.CLASS_NAME, "field_errors")) != 0:
           allure.attach(driver.get_screenshot_as_png(),
                              name="Invalid Authorization", attachment_type=allure.attachment_type.PNG)
    
    @allure.description("Sign up Label Studio with not fill field login")  
    @allure.severity(severity_level = "NORMAL")  
    def test_not_fill_out_sign_up(self, test_setup):
        signupLabels = WebDriverWait(driver, timeout=20).until(lambda d: d.find_elements(By.TAG_NAME,"a"))
        signupLabels[0].click()
        
        with allure.step("Not fill email"):
            email = driver.find_element(By.ID,'email')
            email.send_keys("")
            
        with allure.step("Not fill password"):
            password = driver.find_element(By.ID,'password')
            password .send_keys("")
        signup_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
        signup_button.click()
        driver.implicitly_wait(60)
        # Check alert error
        if len(driver.find_elements(By.CLASS_NAME, "field_errors")) == 2:
            allure.attach(driver.get_screenshot_as_png(),
                              name="Invalid Authorization", attachment_type=allure.attachment_type.PNG)
        