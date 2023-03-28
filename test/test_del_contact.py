import random

from model.contact import Contact
from random import randrange


def test_delete_some_contact(app, db):
    if len(db.get_group_list()) == 0:
        app.contact.create_new_contact(Contact(firstname="DIMA TEST"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count_contact()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
