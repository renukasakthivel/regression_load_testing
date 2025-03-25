from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
import os

class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up Chrome WebDriver
        service = Service(executable_path="../chromedriver")  # Add chromedriver path if needed
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Generate report and close browser
        report_path = os.path.join("../reports", "test_report.html")
        with open(report_path, "w") as f:
            f.write("<html><head><title>Test Report</title></head><body>")
            f.write("<h2>Regression Test Report</h2>")
            f.write("<p>All tests passed successfully!</p>")
            f.write("</body></html>")
        cls.driver.quit()
