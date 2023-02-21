from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact((Contact(firstname="edit", middlename="edit", lastname="edit", nickname="alex2", title="zagolovok", company="corporation umbrella", address="vyzov",
                                home="edit.bil", mobile="9800089899", work="sdfsd", fax="97878792342342", email="edit@edit.ru", homepage="www.ya.ru", bday="1",
                                amonth="January", byear="1980", bmonth="January", aday="8", ayear="1990", address2="sdsadsa", phone2="sdadas", notes="asdasd")))
    app.session.logout()