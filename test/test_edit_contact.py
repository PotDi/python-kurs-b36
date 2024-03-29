from model.contact import Contact
import random


def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(firstname="THIS IS TEST"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_edit = Contact(firstname="HELLO DIMA", lastname="test")
    contact_edit.id = contact.id
    app.contact.edit_contact_by_id(contact.id, contact_edit)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(contact_edit)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(
            app.contact.get_contact_list(), key=Contact.id_or_max)
