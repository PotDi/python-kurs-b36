from model.contact import Contact
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(bday="1", amonth="January", byear="1980", bmonth="January",
                    aday="8", ayear="1990")] + \
           [Contact(firstname=random_string("firstname", 7), middlename=random_string("middlename", 8),
                    lastname=random_string("lastname", 7), nickname=random_string("nickname", 5), title=random_string("title", 10),
                    company=random_string("firstname", 10), address=random_string("address", 15),
                    homephone=random_string("homephone", 6), mobilephone=random_string("mobilephone", 10),
                    workphone=random_string("workphone", 6), fax=random_string("fax", 6), email=random_string("email", 6),
                    secondaryemail=random_string("secondaryemail", 6), homepage=random_string("homepage", 6),
                    secondaryaddress=random_string("secondaryaddress", 6), secondaryphone=random_string("secondaryaddress", 10),
                    notes=random_string("notes", 20))
            for i in range(5)

            ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
