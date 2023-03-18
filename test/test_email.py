def test_email_home_page(app):
    email_from_home_page = app.contact.get_contact_list()[0]
    email_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert email_from_home_page.all_email_from_home_page == merge_all_email_like_home_page(email_from_edit_page)


def merge_all_email_like_home_page(contact):
    return "\n".join(filter(lambda x: x != "",  # фильтруем пустые строки и потом склеиваем при помощи перевода строки
                            filter(lambda x: x is not None,  # фильтруем все пустые значения
                                   [contact.email, contact.secondaryemail,
                                    contact.thirdemail])))  # получаем исходный список
