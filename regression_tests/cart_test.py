from base import BaseTest
from selenium.webdriver.common.by import By
import time

class CartTest(BaseTest):
    def test_add_to_cart(self):
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
        search_box.submit()

        time.sleep(3)  # Wait for results to load

        # Click on the first product
        self.driver.find_element(By.XPATH, '(//div[@class="_4rR01T"])[1]').click()

        # Switch to new tab
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Click on Add to Cart
        self.driver.find_element(By.XPATH, '//button[contains(text(),"ADD TO CART")]').click()
        time.sleep(2)

        # Verify that item is added to cart
        assert "Shopping Cart" in self.driver.title
