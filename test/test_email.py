def test_email_home_page(app):
    email_from_home_page = app.contact.get_contact_list()[0]
    email_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert email_from_home_page.all_email_from_home_page