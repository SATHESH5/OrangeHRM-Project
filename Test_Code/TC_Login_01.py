from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import TC_Logindata_01
import pytest
import time

class Test_Login:
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.close()
        
    def test_login(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=TC_Logindata_01.Login_Selectors.input_box_username).send_keys(TC_Logindata_01.Login_Data.username)
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value=TC_Logindata_01.Login_Selectors.input_box_password).send_keys(TC_Logindata_01.Login_Data.password)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=TC_Logindata_01.Login_Selectors.login_xpath).click()
        time.sleep(3)
        print("The user is logged in successfully")
        
            
            
            
            
            
        
        
        