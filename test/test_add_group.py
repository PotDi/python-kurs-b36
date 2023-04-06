from model.group import Group
# from data.groups import const as testdata
# import pytest


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(map(clear_group, new_groups), key=Group.id_or_max) == \
               sorted(
            app.group.get_group_list(), key=Group.id_or_max)


def clear_group(group):
    _ = clear_space
    return Group(id=group.id, name=_(group.name), header=_(group.header),
                 footer=_(group.footer))


def clear_space(s):
    return " ".join(s.split()) if s is not None else ""