from selenium import webdriver
from selenium.webdriver.common.by import By
from Driver import service

driver = webdriver.Chrome(service=service)


class TestItemClass:

    def test_checkout_login_user(self):
        driver.get("https://magento.softwaretestingboard.com/")
        assert driver.find_element(By.XPATH, "//a[@class='logo']")

