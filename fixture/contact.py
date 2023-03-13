from selenium.webdriver.support.ui import Select
from model.contact import Contact


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

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        #open edit form
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # Fill contact details
        self.fill_contact_form(new_contact_data)
        # submit update contact
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        #submit contact delete
        wd.find_element_by_xpath("//input[@onclick='DeleteSel()']").click()
        wd.switch_to.alert.accept()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("homepage", contact.homepage)
        self.change_list_value("bday", contact.bday)
        self.change_list_value("amonth", contact.amonth)
        self.change_field_value("byear", contact.byear)
        self.change_list_value("bmonth", contact.bmonth)
        self.change_list_value("aday", contact.aday)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
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

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contacts = []
        for element in wd.find_elements_by_xpath("//*[@name='entry']"):
            lastname = element.find_element_by_xpath(".//td[2]").text
            firstname = element.find_element_by_xpath(".//td[3]").text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return contacts
