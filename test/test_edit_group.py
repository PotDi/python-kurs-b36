from model.group import Group


def test_edit_group_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="New group")
    group.id = old_groups[0].id
    if app.group.count_group() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first_group(Group(name="New group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_for_max) == sorted(new_groups, key=Group.id_for_max)


# def test_edit_group_header(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count_group() == 0:
#         app.group.create(Group(header="test"))
#     app.group.edit_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
