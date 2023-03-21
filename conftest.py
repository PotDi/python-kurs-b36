import json
import pytest
from fixture.application import Application
import os.path

fixture = None
conf = None


@pytest.fixture
def app(request):
    global fixture
    global conf
    browser = request.config.getoption("--browser")
    if conf is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--conf"))
        with open(request.config.getoption("--conf")) as f:
            conf = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=conf["baseUrl"])
    fixture.session.ensure_login(username=conf["username"], password=conf["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--conf", action="store", default="conf.json")

