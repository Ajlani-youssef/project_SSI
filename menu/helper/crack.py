import hashlib


def md5(message):
    try:
        fp = open("C:/Users/youss/PycharmProjects/chatRoom/menu/helper/dictionaire.txt")
        line = fp.readline().strip()
        while line:
            msgEncode = line.encode("utf-8")
            result = hashlib.md5(msgEncode).hexdigest()
            if result == message:
                print("Le message craqué : ", line)
                break
            line = fp.readline().strip()
        print('done')
    finally:
        fp.close()


def sha1(message):
    try:
        fp = open("C:/Users/youss/PycharmProjects/chatRoom/menu/helper/dictionaire.txt")
        line = fp.readline().strip()
        while line:
            msgEncode = line.encode("utf-8")
            result = hashlib.sha1(msgEncode).hexdigest()
            if result == message:
                print("Le message craqué : ", line)
                break
            line = fp.readline().strip()
        print('done')
    finally:
        fp.close()


def sha256(message):
    try:
        fp = open("C:/Users/youss/PycharmProjects/chatRoom/menu/helper/dictionaire.txt")
        line = fp.readline().strip()
        while line:
            msgEncode = line.encode("utf-8")
            result = hashlib.sha256(msgEncode).hexdigest()
            if result == message:
                print("Le message craqué : ", line)
                break
            line = fp.readline().strip()
        print('done')
    finally:
        fp.close()
