from model.contact import Contact


def test_edit_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count_contact() == 0:
        app.contact.create_new_contact(Contact(firstname="THIS IS TEST"))
    app.contact.edit_first_contact(Contact(firstname="HELLO DIMA", bmonth="December"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
