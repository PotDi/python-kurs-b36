# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="wewew", middlename="rerfdfdf", lastname="fsdfdsf", nickname="alex", title="zagolovok", company="corporation", address="vyzov",
                                home="rubik.bil", mobile="9800089899", work="sdfsd", fax="9787879", email="sdfsd@sasd.ru", homepage="www.ya.ru", bday="1",
                                amonth="January", byear="1980", bmonth="January", aday="8", ayear="1990", address2="sdsadsa", phone2="sdadas", notes="asdasd")
    app.contact.create_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
