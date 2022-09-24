"""
This script is used to show Selenium usage for LinkedIn Automation
"""

from selenium import webdriver
from time import sleep


class Linkedin(object):
    # constructor
    def __init__(self, username, password):
        """
        This is constructor
        :param username: <str> Linkedin email address
        :param password: <str> Linkedin password
        """
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def unfollow_companies(self):
        # get request to sign-in page
        self.browser.get(
            "https://www.linkedin.com/uas/login?fromSignIn=true&trk=cold_join_sign_in"
        )
        sleep(2)
        # pass username and password
        self.browser.find_element_by_id("username").send_keys(self.username)
        self.browser.find_element_by_id("password").send_keys(self.password)
        sleep(3)
        # click login
        self.browser.find_element_by_xpath(
            '//*[@id="organic-div"]/form/div[3]/button').click()
        sleep(1)
        # redirect to companies you followed page
        self.browser.get(
            "https://www.linkedin.com/feed/following/?filterType=company")
        sleep(2)
        companies = list()
        # scroll page to see all companies in dynamic HTML
        SCROLL_PAUSE_TIME = 0.5
        last_height = self.browser.execute_script(
            "return document.body.scrollHeigh")
        while True:
            # scroll down to bottom
            self.browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

            # wait to load page
            sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.browser.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            # scroll ended here
        # wait 3 seconds to load page
        sleep(3)
        # retrieve all companies
        companies = self.browser.find_elements_by_css_selector(
            'button[class*="follow is-following  follows-recommendation-card__follow-btn artdeco-button artdeco-button--tertiary artdeco-button--1 artdeco-button--fluid"]'
        )
        # unfollow all companies
        for company in companies:
            webdriver.ActionChains(
                self.browser).move_to_element(company).click(company).perform()
            sleep(1)


if __name__ == "__main__":
    obj_linkedin = Linkedin("your_email", "your_password")
