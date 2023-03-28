from model.contact import Contact
import random
import calendar
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts",
                                                      "file"])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10 #можно
    # добавить string.punctuation, но тогда тесты будут падать
    return prefix + "".join(
        [random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_day():
    day = random.randint(1, 31)
    return str(day)


def random_year():
    year = random.randint(0, 9999)
    return str(year)


def random_month():
    num = random.randrange(1, 12)
    return calendar.month_name[num]


testdata = [Contact(firstname="",
                    middlename="",
                    lastname="",
                    nickname="",
                    title="",
                    company="",
                    address="",
                    homephone="",
                    mobilephone="",
                    workphone="",
                    fax="",
                    email="",
                    secondaryemail="",
                    thirdemail="",
                    homepage="",
                    bday="",
                    amonth="-",
                    byear="",
                    bmonth="-",
                    aday="",
                    ayear="",
                    secondaryaddress="",
                    secondaryphone="",
                    notes="")] + \
           [Contact(firstname=random_string("firstname", 7),
                    middlename=random_string("middlename", 8),
                    lastname=random_string("lastname", 7),
                    nickname=random_string("nickname", 5),
                    title=random_string("title", 10),
                    company=random_string("firstname", 10),
                    address=random_string("address", 15),
                    homephone=random_string("homephone", 6),
                    mobilephone=random_string("mobilephone", 10),
                    workphone=random_string("workphone", 6),
                    fax=random_string("fax", 6),
                    email=random_string("email", 6),
                    secondaryemail=random_string("secondaryemail", 6),
                    thirdemail=random_string("thirdemail", 7),
                    homepage=random_string("homepage", 6),
                    bday=random_day(),
                    amonth=random_month(),
                    byear=random_year(),
                    bmonth=random_month(),
                    aday=random_day(),
                    ayear=random_year(),
                    secondaryaddress=random_string("secondaryaddress", 6),
                    secondaryphone=random_string("secondaryaddress", 10),
                    notes=random_string("notes", 20))
            for i in range(5)
            ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
