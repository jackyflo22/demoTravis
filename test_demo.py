from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


class TestItemClass:

    def test_checkout_login_user(self):
        driver.get("https://magento.softwaretestingboard.com/")
        assert driver.find_element(By.XPATH, "//a[@class='logo']")

