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
        self.black = ["iiitbhopalmeme"]
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

        self.posts = self.driver.find_elements_by_xpath("//article[contains(@class, '_8Rm4L')]")
        self.heart_sec = self.driver.find_elements_by_xpath("//span[contains(@class, 'fr66n')]")
        self.following_sec = self.driver.find_elements_by_xpath("//div[contains(@class, 'eleld')]")

        for ele in self.posts:
            self.heart=ele.find_element_by_class_name("eo2As").find_element_by_class_name("ltpMr").find_element_by_class_name("fr66n").find_element_by_tag_name("button")
            self.colour=self.heart.find_element_by_tag_name("svg").get_attribute("fill")
            self.username=ele.find_element_by_tag_name("header").find_element_by_class_name("o-MQd").find_element_by_class_name("RqtMr").find_element_by_class_name("e1e1d").find_element_by_tag_name("a").text

            if self.blacklist(self.username):
                continue
            else:
                if self.colour == "#262626":
                    self.heart.click()
                else:
                    break


    def blacklist(self, username):
        if username in self.black:
            return True
        else:
            return False



    def check_exists_by_xpath(self, xpath):
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return True
        return False


username = input("Enter your username: ")
password = input("Enter your passwore: ")
obj=Instabot(username, password)
obj.login()
obj.like()
