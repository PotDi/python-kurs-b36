from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    contacts = db.get_contacts_in_group(group)
    if not contacts:
        app.contact.create_new_contact(Contact(firstname="THIS IS TEST"))
        contacts = db.get_contact_list()
        app.contact.add_contact_in_group(contacts.id, group.id)
        contacts = db.get_contacts_in_group(group)
    contact = random.choice(contacts)
    app.contact.del_contact_from_group(contact.id, group.id)
    assert clear_contact_db(contact) in db.get_contacts_without_group(group)


def clear(s):
    return "" if s is None else s


def clear_contact_db(contact):
    _ = clear
    return Contact(firstname=_(contact.firstname),
                   middlename=contact.middlename,
                   lastname=_(contact.lastname), nickname=contact.nickname,
                   title=contact.title, company=contact.company,
                   address=_(contact.address), mobilephone=_(
            contact.mobilephone),
                   homephone=_(contact.homephone), workphone=_(
            contact.workphone),
                   fax=_(contact.fax), email=_(contact.email),
                   secondaryemail=_(contact.secondaryemail),
                   homepage=_(contact.homepage), bday=_(contact.bday),
                   bmonth=_(contact.bmonth),
                   byear=_(contact.byear), aday=_(contact.aday),
                   amonth=_(contact.amonth), ayear=_(contact.ayear),
                   secondaryaddress=_(contact.secondaryaddress),
                   secondaryphone=_(
            contact.secondaryphone),
                   notes=_(contact.notes), id=_(contact.id))
