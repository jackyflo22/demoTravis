from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())


class TestItemClass:

    def test_checkout_login_user(self):
        driver.get("https://magento.softwaretestingboard.com/")
        assert driver.find_element(By.XPATH, "//a[@class='logo']")

