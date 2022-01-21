import re

from utils.dao import Dao
from utils.doublefactor import send_verification_code


def login():
    dao = Dao()
    print("enter email")
    email = input()
    print("enter password")
    password = input()
    if dao.login(email, password):
        code = send_verification_code(email)
        verification_code = int(input("Enter your verification code:"))
        if verification_code == code:
            print("authenticated")
            return True
        else:
            print("please try again")
            return False
    else:
        print("please try again")
        return False