from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import urllib.request

class Instabot:
    def __init__(self, username, pw):
        self.username=username
        self.pw=pw
        self.black = ["iiitbhopalmeme"]
        self.save_list = ["dp._photos"]
        self.driver=webdriver.Firefox()
        self.driver.get("https://instagram.com")
        time.sleep(2)


    def login(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(self.username)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(self.pw)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()

    def like(self):
        self.driver.implicitly_wait(10)

        self.posts = self.driver.find_elements_by_xpath("//article[contains(@class, '_8Rm4L')]")
        self.heart_sec = self.driver.find_elements_by_xpath("//span[contains(@class, 'fr66n')]")

        for post in self.posts:
            self.heart = post.find_element_by_class_name("eo2As").find_element_by_class_name("ltpMr").find_element_by_class_name("fr66n").find_element_by_tag_name("button")
            self.colour = self.heart.find_element_by_tag_name("svg").get_attribute("fill")
            self.user = post.find_element_by_tag_name("header").find_element_by_class_name("o-MQd").find_element_by_class_name("RqtMr").find_element_by_class_name("e1e1d").find_element_by_tag_name("a").text

            if self.blacklist(self.user):
                continue
            else:
                if self.colour == "#262626":
                    self.heart.click()
                else:
                    break

    def save(self):
        self.driver.implicitly_wait(10)
        print("1")
        self.posts = self.driver.find_elements_by_xpath("//article[contains(@class, '_8Rm4L')]")

        for post in self.posts:
            self.user = post.find_element_by_tag_name("header").find_element_by_class_name("o-MQd").find_element_by_class_name("RqtMr").find_element_by_class_name("e1e1d").find_element_by_tag_name("a").text
            print(self.user)
            
            if self.user in self.save_list:
                print("2.5")
                # if self.check_exists_by_class(post.find_element_by_class_name("_97aPb").find_element_by_tag_name("div"), "kPFhm"):
                #      continue                    
                # else:
                print("3")
                self.image_url = post.find_element_by_class_name("_97aPb").find_element_by_class_name("ZyFrc").find_element_by_class_name("eLAPa").find_element_by_class_name("KL4Bh").find_element_by_tag_name("img").get_attribute("src")
                urllib.request.urlretrieve(self.image_url, "images/"+self.user+".jpg")
                
                break

    def blacklist(self, username):
        if username in self.black:
            return True
        else:
            return False



    def check_exists_by_class(self, path, class_name):
        self.driver.implicitly_wait(10)
        try:
            path.find_element_by_class_name(class_name)
        except NoSuchElementException:
            return False
        return True


username = input("Enter your username: ")
password = input("Enter your password: ")
obj=Instabot(username, password)
obj.login()
#obj.like()
obj.save()
