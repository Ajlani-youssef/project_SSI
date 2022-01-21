from menu.menu import menu
from signup.sign_up import sign_up
from login.login import login

if __name__ == '__main__':
    while 1:
        print("1-login")
        print("2-sign up")
        print("3-quit")
        choice = int(input())
        if choice == 1:
            # if login():
                menu()
        elif choice == 2:
            sign_up()
        elif choice == 3:
            exit()
        else:
            print("choose correct answer")
