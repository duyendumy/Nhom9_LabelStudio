from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest

class TestSingUp():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="D:/Cong cu va Moi truong phat trien phan mem/chromedriver/chromdriver.exe")
        driver.implicitly_wait(15)
        driver.maximize_window
        driver.get("http://localhost:8080")
        yield
        driver.close()
        driver.quit()
    
    def test_signup_by_existing_account(self, test_setup):
        signupLabels = WebDriverWait(driver, timeout=20).until(lambda d: d.find_elements(By.TAG_NAME,"a"))
        signupLabels[0].click()
        email = driver.find_element(By.ID,'email')
        # Send existing email
        email.send_keys("labelstudio09@gmail.com")
        password = driver.find_element(By.ID,'password')
        # Send existing password
        password .send_keys("1234asdfASDF")
        signup_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
        signup_button.click()
        driver.implicitly_wait(60)
        # Check alert error
        if len(driver.find_elements(By.CLASS_NAME, "field_errors")) != 0:
            print("Alert error 'User with this email already exists'")
    
    def test_not_fill_out_sign_up(self, test_setup):
        signupLabels = WebDriverWait(driver, timeout=20).until(lambda d: d.find_elements(By.TAG_NAME,"a"))
        signupLabels[0].click()
        email = driver.find_element(By.ID,'email')
        email.send_keys("")
        password = driver.find_element(By.ID,'password')
        password .send_keys("")
        signup_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
        signup_button.click()
        driver.implicitly_wait(60)
        # Check alert error
        if len(driver.find_elements(By.CLASS_NAME, "field_errors")) == 2:
            print("Alert error 'Invalid email'")
            print("Alert error 'Please enter a password 8-12 characters in length'")