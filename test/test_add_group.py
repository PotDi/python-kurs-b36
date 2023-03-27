from model.group import Group
# from data.groups import const as testdata
# import pytest

#закомментировал так тестовые данные генерятся  отдельно, а потом берутся из
# Json
# файла в
#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    # assert len(old_groups) + 1 == app.group.count_group() больше не нужна
    # такая проверка, т.к. загрузка списка выполняется быстрее и данное
    # хеширование не нужно.
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)