from base import BaseTest
from selenium.webdriver.common.by import By

class LoginTest(BaseTest):
    def test_valid_login(self):
        self.driver.get("https://www.flipkart.com/")
        
        # Close login popup if visible
        try:
            close_button = self.driver.find_element(By.XPATH, '//button[contains(text(),"✕")]')
            close_button.click()
        except:
            pass
        
        # Click on Login button
        login_button = self.driver.find_element(By.LINK_TEXT, "Login")
        login_button.click()

        # Enter credentials
        self.driver.find_element(By.XPATH, '//input[@type="text"]').send_keys("testuser@gmail.com")
        self.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys("testpassword")

        # Click login
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()

        # Check if login successful
        self.assertIn("Flipkart", self.driver.title)
