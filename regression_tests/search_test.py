from base import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class SearchTest(BaseTest):
    def test_search_product(self):
        self.driver.get("https://www.flipkart.com/")

        # Close login popup if visible
        try:
            close_button = self.driver.find_element(By.XPATH, '//button[contains(text(),"✕")]')
            close_button.click()
        except:
            pass

        # Search for a product
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("laptop")
        search_box.send_keys(Keys.RETURN)

        time.sleep(3)  # Wait for search results to load

        # Verify search results loaded
        assert "laptop" in self.driver.title.lower()
