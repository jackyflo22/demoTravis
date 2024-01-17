from selenium.webdriver.common.by import By

from Driver import Driver

driver = Driver().get_webdriver_instance()


class TestItemClass:

    def test_checkout_login_user(self):
        driver.get("https://magento.softwaretestingboard.com/")
        assert driver.find_element(By.XPATH, "//a[@class='logo']")

