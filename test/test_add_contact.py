# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new_contact(Contact(firstname="wewew", middlename="rerfdfdf", lastname="fsdfdsf", nickname="alex", title="zagolovok", company="corporation", address="vyzov",
                                home="rubik.bil", mobile="9800089899", work="sdfsd", fax="9787879", email="sdfsd@sasd.ru", homepage="www.ya.ru", bday="1",
                                amonth="January", byear="1980", bmonth="January", aday="8", ayear="1990", address2="sdsadsa", phone2="sdadas", notes="asdasd"))
    app.session.logout()
