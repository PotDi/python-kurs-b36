import random

from model.group import Group
from random import randrange


def test_edit_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_edit_name = Group(name="New group")
    group_edit_name.id = group.id
    app.group.edit_group_by_id(group.id, group_edit_name)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(group_edit_name)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_group_header(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count_group() == 0:
#         app.group.create(Group(header="test"))
#     app.group.edit_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
