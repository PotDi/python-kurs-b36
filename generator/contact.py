from model.contact import Contact
import random
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
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(bday="1", amonth="January", byear="1980", bmonth="January",
                    aday="8", ayear="1990")] + \
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
                    secondaryaddress=random_string("secondaryaddress", 6),
                    secondaryphone=random_string("secondaryaddress", 10),
                    notes=random_string("notes", 20))
            for i in range(5)
            ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))