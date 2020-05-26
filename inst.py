from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

class Instabot:
    def __init__(self, username, pw):
        self.username=username
        self.pw=pw
        self.driver=webdriver.Firefox()
        self.driver.get("https://instagram.com")
        time.sleep(2)


    def login(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(self.username)
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(self.pw)
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
        time.sleep(2)

    def like(self):
        self.driver.implicitly_wait(10)

        self.heart_sec = self.driver.find_elements_by_xpath("//span[contains(@class, 'fr66n')]")

        for ele in self.heart_sec:
            self.heart=ele.find_element_by_tag_name("button")
            self.colour=self.heart.find_element_by_tag_name("svg").get_attribute("fill")

            if self.colour == "#262626":
                self.heart.click()
            else:
                break



    def check_exists_by_xpath(self, xpath):
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return True
        return False


obj=Instabot("prashant_0_9_", "helloworld")
obj.login()
obj.like()
