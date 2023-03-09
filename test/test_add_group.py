from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="sdhfsdf", header="sdfsdf", footer="sdfdsdf")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_empty_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)