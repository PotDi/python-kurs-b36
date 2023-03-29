import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name,
                                          user=user, password=password,
                                          autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, "
                           "group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row  # Так же можно использовать
                # конструкцию for row in cursor.fetchall():
                list.append(Group(id=str(id), name=name, header=header,
                                  footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        contacts = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, "
                           "nickname, company, title, address, home, "
                           "mobile, work, fax, email, email2, email3, "
                           "homepage, bday, byear, aday, amonth, ayear, "
                           "address2, phone2, notes from "
                           "addressbook where deprecated='0000-00-00 "
                           "00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company,
                 title, address, homephone, mobilephone, workphone, fax,
                 email, secondaryemail, thirdemail, homepage, bday, byear,
                 aday, amonth, ayear, secondaryaddress, secondaryphone, notes
                 ) = row
                contacts.append(Contact(id=str(id), firstname=firstname,
                                        middlename=middlename,
                                        lastname=lastname, nickname=nickname,
                                        company=company, title=title,
                                        address=address, homephone=homephone,
                                        mobilephone=mobilephone,
                                        workphone=workphone, fax=fax,
                                        email=email,
                                        secondaryemail=secondaryemail,
                                        thirdemail=thirdemail,
                                        homepage=homepage, bday=bday,
                                        byear=byear, aday=aday,
                                        amonth=amonth, ayear=ayear,
                                        secondaryaddress=secondaryaddress,
                                        secondaryphone=secondaryphone,
                                        notes=notes))
        finally:
            cursor.close()
        return contacts

    def destroy(self):
        self.connection.close()
