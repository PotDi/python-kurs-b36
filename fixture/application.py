from selenium import webdriver
from selenium.webdriver.common.by import By

from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
#       self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url
        self.groups_page = "group.php"
        self.group_page = "/?group="

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("searchform")) > 0):
            wd.get(self.base_url)

    def go_group_page(self, id):
        wd = self.wd
        groups_page = self.groups_page + id
        if not (wd.current_url.endswith(groups_page) and len(
            wd.find_elements_by_css_selector("div[class='msgbox'")) > 0):
            wd.find_element(By.PARTIAL_LINK_TEXT, "group page").click()

    def open_page_new_contact(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        wd.current_url.endswith("/edit.php")

    def destroy(self):
        self.wd.quit()
