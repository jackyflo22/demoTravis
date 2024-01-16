from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

class TestItemClass:

    def test_checkout_login_user(self):
        driver.get("https://magento.softwaretestingboard.com/")
        assert driver.find_element(By.XPATH, "//a[@class='logo']")

