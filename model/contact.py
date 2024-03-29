from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None,
                 nickname=None, title=None, company=None,
                 address=None, homephone=None, mobilephone=None,
                 workphone=None, fax=None,
                 email=None, secondaryemail=None, thirdemail=None,
                 homepage=None, bday=None, amonth=None, byear=None,
                 bmonth=None,
                 aday=None, ayear=None, add_group=None, secondaryaddress=None,
                 secondaryphone=None,
                 notes=None, id=None, all_phones_from_home_page=None,
                 all_email_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.secondaryemail = secondaryemail
        self.thirdemail = thirdemail
        self.homepage = homepage
        self.bday = bday
        self.amonth = amonth
        self.byear = byear
        self.bmonth = bmonth
        self.aday = aday
        self.ayear = ayear
        self.add_group = add_group
        self.secondaryaddress = secondaryaddress
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page

    def __repr__(self):
        return "%s %s %s %s" % (self.id, self.firstname,
                                self.lastname, self.middlename)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (
                           self.firstname == other.firstname or self.firstname is None
                           or other.firstname is None) and \
               (self.lastname == other.lastname or self.lastname is None
                or other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
