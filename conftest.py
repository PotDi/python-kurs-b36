import json
import pytest
from fixture.application import Application
import os.path
import importlib
import jsonpickle
from fixture.db import DbFixture
from fixture.orm import ORMFixture

fixture = None
conf = None


def load_config(file):
    global conf
    if conf is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   file)
        with open(config_file) as config_file:
            conf = json.load(config_file)
    return conf


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--conf"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["baseUrl"])
    fixture.session.ensure_login(username=web_config["username"],
                                 password=web_config["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def db(request):
    db_config = load_config(request.config.getoption("--conf"))['db']
    dbfixture = ORMFixture(host=db_config['host'], name=db_config['name'],
                          user=db_config['user'], password=db_config[
            'password'])
    # def fin():
    #     dbfixture.destroy()
    # request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--ui")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--conf", action="store", default="conf.json")
    parser.addoption("--ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())
