import re


def test_property_contact_on_home_page(app):
    property_contact_from_home_page = app.contact.get_contact_list()[0]
    property_contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert property_contact_from_home_page.firstname == property_contact_from_edit_page.firstname
    assert property_contact_from_home_page.lastname == property_contact_from_edit_page.lastname
    assert property_contact_from_edit_page.address == property_contact_from_home_page.address
    assert property_contact_from_home_page.all_email_from_home_page == merge_all_email_like_home_page(
        property_contact_from_edit_page)
    assert property_contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(
        property_contact_from_edit_page)


def test_phone_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert clear_space(contact_from_view_page.homephone) == contact_from_edit_page.homephone
    assert clear_space(contact_from_view_page.workphone) == contact_from_edit_page.workphone
    assert clear_space(contact_from_view_page.mobilephone) == contact_from_edit_page.mobilephone
    assert clear_space(contact_from_view_page.secondaryphone) == contact_from_edit_page.secondaryphone


# def test_phones_on_home_page(app):
#     contact_from_home_page = app.contact.get_contact_list()[0]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
#     assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)
#     assert contact_from_home_page.mobilephone == clear(contact_from_edit_page.mobilephone)
#     assert contact_from_home_page.secondaryphone == clear(contact_from_edit_page.secondaryphone)
def clear(s):
    return re.sub(r"[. / -]", "", s)


def clear_space(s):
    return s.lstrip()


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",  # фильтруем пустые строки и потом склеиваем при помощи перевода строки
                            map(lambda x: clear(x),  # удаляем все лишние символы
                                filter(lambda x: x is not None,  # фильтруем все пустые значения
                                       [contact.homephone, contact.mobilephone, contact.workphone,
                                        contact.secondaryphone]))))  # получаем исходный список


def merge_all_email_like_home_page(contact):
    return "\n".join(filter(lambda x: x != "",  # фильтруем пустые строки и потом склеиваем при помощи перевода строки
                            filter(lambda x: x is not None,  # фильтруем все пустые значения
                                   [contact.email, contact.secondaryemail,
                                    contact.thirdemail])))  # получаем исходный список
