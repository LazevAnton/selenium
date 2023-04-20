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
    REGISTER_URL = f'{BASE_URL}/auth/register'

    def __int__(self):
        self.driver = None

    def create_driver(self):
        try:
            self.driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)
            self.driver.maximize_window()
            return self.driver
        except Exception as e:
            print(e.args)

    def social_network_register(self, username, password, email):
        driver = self.create_driver()
        driver.get(self.REGISTER_URL)
        username_form = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@class='form-control']"
                                                      "[@id='username']")
        username_form.send_keys(username)
        time.sleep(1)
        email_form = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@class='form-control']"
                                                   "[@id='email']")
        email_form.send_keys(email)
        time.sleep(1)
        password_form = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@class='form-control']"
                                                      "[@id='password']")
        password_form.send_keys(password)
        time.sleep(1)
        confirm_pass_form = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@class='form-control']"
                                                          "[@id='confirm_password']")
        confirm_pass_form.send_keys(password)
        time.sleep(1)
        register_button = driver.find_element(By.XPATH, "//div[@class='form-group']/button")
        register_button.click()
        return self.driver

    def social_network_login(self):
        driver = self.create_driver()
        driver.get(self.LOGIN_URL)
        username = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='username']")
        username.send_keys(config.SOCIAL_NETWORK_REGISTER_USER)
        password = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='password']")
        password.send_keys(config.SOCIAL_NETWORK_REGISTER_PASSWORD)
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
        time.sleep(3)
        set_like = self.driver.find_element(By.ID, 'post_like')
        set_like.click()
        time.sleep(5)
        logout_button = self.driver.find_element(By.ID, 'logout_btn')
        logout_button.click()
        time.sleep(5)
        return self.driver
