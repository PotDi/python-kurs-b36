from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href=index.php]").click()

    def count_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def create_new_contact(self, contact):
        wd = self.app.wd
        self.app.open_page_new_contact()
        self.fill_contact_form(contact)
        #Submit fill
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        #open edit form
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        # Fill contact details
        self.fill_contact_form(new_contact_data)
        # submit update contact
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        #open edit form
        wd.find_element_by_xpath("//a[contains(@href, "
                                  "'edit.php?id=%s')]" % id).click()
        # Fill contact details
        self.fill_contact_form(new_contact_data)
        # submit update contact
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        #submit contact delete
        wd.find_element_by_xpath("//input[@onclick='DeleteSel()']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        #submit contact delete
        wd.find_element_by_xpath("//input[@onclick='DeleteSel()']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("homepage", contact.homepage)
        self.change_list_value("bday", contact.bday)
        self.change_list_value("amonth", contact.amonth)
        self.change_field_value("byear", contact.byear)
        self.change_list_value("bmonth", contact.bmonth)
        self.change_list_value("aday", contact.aday)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.secondaryaddress)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("notes", contact.notes)

    def change_list_value(self, list_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(list_name).click()
            Select(wd.find_element_by_name(list_name)).select_by_visible_text(value)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//*[@name='entry']"):
                lastname = element.find_element_by_xpath(".//td[2]").text
                firstname = element.find_element_by_xpath(".//td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                address = element.find_element_by_xpath(".//td[4]").text
                all_email = element.find_element_by_xpath(".//td[5]").text
                all_phones = element.find_element_by_xpath(".//td[6]").text
                self.contact_cache.append(Contact(lastname=lastname,
                                                  firstname=firstname, id=id,
                                                  all_phones_from_home_page=all_phones, address=address,
                                                  all_email_from_home_page=all_email))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        secondaryemail = wd.find_element_by_name("email2").get_attribute("value")
        thirdemail = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone,
                       address=address, email=email,
                       secondaryemail=secondaryemail, thirdemail=thirdemail)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H:(.*)", text).group(1)
        mobilephone = re.search("M:(.*)", text).group(1)
        workphone = re.search("W:(.*)", text).group(1)
        secondaryphone = re.search("P:(.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def add_group_in_contact(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact_id)
        select = Select(wd.find_element_by_name("to_group"))
        select.select_by_value("75")
        wd.find_element_by_name("add").click()
        wd.find_element_by_xpath("//a[@href='./?group='75']").click()
        self.contact_cache = None


