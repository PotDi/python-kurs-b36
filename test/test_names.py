def test_names_on_home_page(app):
    name_from_home_page = app.contact.get_contact_list()[0]
    name_form_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert name_from_home_page.firstname == name_form_edit_page.firstname
    assert name_from_home_page.lastname == name_form_edit_page.lastname
