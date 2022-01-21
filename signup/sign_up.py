import re

from utils.dao import Dao


def sign_up():
    dao = Dao()
    print("enter first name")
    firstName = input()
    print("enter last name")
    lastName = input()
    print("enter email")
    email = input()
    motif = r"^[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*@[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*(\.[a-zA-Z]{2,6})$"
    while (re.match(motif, email) is None) or (dao.search_user_by_email(email) is not None):
        if re.match(motif, email) is None:
            print("re-enter email")
        else:
            print("email already exist")
        email = input()
    password1 = input("enter password")
    password2 = input("re-enter password")
    while password1 != password2:
        password2 = input("wrong password,verify ")
    dao.add_user(firstName, lastName, email, password2)
    print("registered successfully")
