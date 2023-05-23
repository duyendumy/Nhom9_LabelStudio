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

class TestLabelData():
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
        
    @pytest.fixture()
    @allure.description("Open Cloud Storage Of Project")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_open_label_interface(self,test_setup):
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
        
        with allure.step("Click Labeling Interface"):    
            list_main_menu_item = driver.find_elements(By.CLASS_NAME, "ls-main-menu__item")
            for item in list_main_menu_item:
                if item.text == "Labeling Interface":
                    item.click()
                    break
                
    @allure.description("Select browse Template")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_select_browse_template(self,test_open_label_interface):
        with allure.step("Click Browse Templates"):  
            template = driver.find_element(By.XPATH, '//button[text()="Browse Templates"]')
            template.click()
        with allure.step("Click Object Detection with Bounding Boxes Template"):  
            driver.implicitly_wait(15)
            list_labeling_interface= driver.find_elements(By.CLASS_NAME, "ls-templates-list__template")
            for item in list_labeling_interface:
                if item.text == "Object Detection with Bounding Boxes":
                    item.click()
                    break
    
    @allure.description("Add Label Name")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_add_label_names(self,test_open_label_interface):
        with allure.step("Enter label name"):  
            input_label_name = driver.find_element(By.NAME,'labels')
            input_label_name.send_keys("Test Label Name")
        with allure.step("Click Add button"): 
            add_btn = driver.find_element(By.XPATH, '//input[contains(@value,"Add")]')
            add_btn.click()
        with allure.step("Click Save button"): 
            save_btn = driver.find_element(By.XPATH, '//button[contains(@class, "ls-button_look_primary") and text()="Save"]')
            save_btn.click()
            
    @allure.description("Delete Label Name")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_delete_label_names(self,test_open_label_interface):
        with allure.step("Click delete label name"):  
            deleteBtn = driver.find_element(By.XPATH, '//button[contains(@class, "ls-configure__delete-label")][1]')
            deleteBtn.click()
        with allure.step("Click Save button"): 
            save_btn = driver.find_element(By.XPATH, '//button[contains(@class, "ls-button_look_primary") and text()="Save"]')
            save_btn.click()
    
    @allure.description("Change Label Color")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_change_label_color(self,test_open_label_interface):
        with allure.step("Change label color"):  
            driver.implicitly_wait(20)
            list_color_labels= driver.find_elements(By.CLASS_NAME, "ls-configure__label-color")
            for item in list_color_labels:         
                item.send_keys("#ff0000")
                break
        with allure.step("Click Save button"): 
            save_btn = driver.find_element(By.XPATH, '//button[contains(@class, "ls-button_look_primary") and text()="Save"]')
            save_btn.click()
            
    @allure.description("Zoom In Image")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_zoom_in_image(self,test_open_label_interface):
        with allure.step("Select Show controls to zoom in and out"):  
            list_checkbox = driver.find_elements(By.CSS_SELECTOR,"label input[type='checkbox']")
            list_checkbox[1].click()
            zoom_in_btn = driver.find_element(By.CSS_SELECTOR,'button[aria-label="zoom-in"]')
            zoom_in_btn.click()
    
    @allure.description("Zoom Out Image")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_zoom_out_image(self,test_open_label_interface):
        with allure.step("Select Show controls to zoom in and out"):  
            list_checkbox = driver.find_elements(By.CSS_SELECTOR,"label input[type='checkbox']")
            list_checkbox[1].click()
            zoom_out_btn = driver.find_element(By.CSS_SELECTOR,'button[aria-label="zoom-out"]')
            zoom_out_btn.click()