from menu.helper.chat import PeerToPeer

from menu.helper import encodedecode

from menu.helper import hash

from menu.helper import crack

from menu.helper import asym


def menu():
    while 1:
        print("1-encoding")
        print("2-hash")
        print("3-cracking")
        print("4-symmetric encryption")
        print("5-asymmetric encryption")
        print("6-chat")
        print("7-quit")
        choice = int(input())
        if choice == 1:
            print("1-encode")
            print("2-decode")
            choice1 = int(input())
            message = input(" enter your message ")
            if choice1 == 1:
                encodedecode.encode(message)
            elif choice1 == 2:
                encodedecode.decode(message)
            else:
                print("wrong choice")
        elif choice == 2:
            print("1-md5")
            print("2-sha1")
            print("3-sha256")
            choice1 = int(input())
            message = input(" enter your message ")
            if choice1 == 1:
                hash.md5(message)
            elif choice1 == 2:
                hash.sha1(message)
            elif choice1 == 3:
                hash.sha256(message)
            else:
                print("wrong choice")
        elif choice == 3:
            print("1-md5")
            print("2-sha1")
            print("3-sha256")
            choice1 = int(input())
            message = input(" enter your message ")
            if choice1 == 1:
                crack.md5(message)
            elif choice1 == 2:
                crack.sha1(message)
            elif choice1 == 3:
                crack.sha256(message)
            else:
                print("wrong choice")
        elif choice == 4:
            print(4)
        elif choice == 5:
            print("1-crypt rsa")
            print("2-decrypt rsa")
            choice1 = int(input())
            message = input(" enter your message ")
            if choice1 == 1:
                asym.encrypt_rsa(message)
            elif choice1 == 2:
                asym.decrypt_rsa(message)
            else:
                print("wrong choice")
        elif choice == 6:
            client = PeerToPeer()
            client.menu()
        elif choice == 7:
            exit()
        else:
            print("choose correct answer")
