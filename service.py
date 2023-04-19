import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import config


class SocialNetworkScraper:
    BASE_URL = f'{config.SOCIAL_NETWORK_HOST}:{config.SOCIAL_NETWORK_PORT}'
    LOGIN_URL = f'{BASE_URL}/auth/login'
    BLOG_URL = f'{BASE_URL}/user/blog'

    def __int__(self):
        self.driver = None

    def create_driver(self):
        try:
            self.driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)
            return self.driver
        except Exception as e:
            print(e.args)

    def social_network_login(self):
        driver = self.create_driver()
        driver.get(self.LOGIN_URL)
        username = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='username']")
        username.send_keys(config.SOCIAL_NETWORK_LOGIN)
        password = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='password']")
        password.send_keys(config.SOCIAL_NETWORK_PASSWORD)
        password.send_keys(keys.Keys.ENTER)
        return driver

    def create_post(self, title, content, login_required=True):
        if login_required:
            self.social_network_login()
        self.driver.get(self.BLOG_URL)
        time.sleep(1)
        title_form = self.driver.find_element(By.XPATH,
                                              "//div[@class='form-group']/input[@class='form-control'][@id='title']")
        title_form.send_keys(title)
        time.sleep(2)
        content_form = self.driver.find_element(By.XPATH,
                                                "//div[@class='form-group']/textarea[@class='form-control']"
                                                "[@id='content']")
        content_form.send_keys(content)
        time.sleep(2)
        create_post_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        create_post_button.click()
        time.sleep(2)
        return self.driver