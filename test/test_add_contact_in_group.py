import random

from model.contact import Contact
from model.group import Group


def test_add_contact_in_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(firstname="THIS IS TEST"))
    contacts = db.get_contacts_without_group(group)
    contact = random.choice(contacts)
    app.contact.add_group_in_contact(contact.id, group.id)

