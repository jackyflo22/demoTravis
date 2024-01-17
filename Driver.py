"""Base Driver Class for WebDriver"""
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as GeckoService
from selenium.webdriver.remote.file_detector import LocalFileDetector
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import config


class Driver:

    @staticmethod
    def get_webdriver_instance():
        """
        Create a driver instance
        :return: driver instance
        """
        options = webdriver.ChromeOptions()
        options.add_argument("window-size=1920,1080")
        options.add_argument("whitelisted-ips")
        options.add_argument('no-sandbox')
        options.add_argument("disable-extensions")
        options.add_argument("--no-proxy-server")
        options.add_argument("--ignore-certificate-errors")  # ignore ssl errors
        options.add_argument("--disable-dev-shm-usage")  # ignore shm usage (Linux related config)
        options.add_argument("--ignore-urlfetcher-cert-requests")  # ignore URL cert request fetch


        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options, keep_alive=True)

        return driver
