import hashlib


def md5(message):
    print(hashlib.md5(message.encode()).hexdigest())


def sha1(message):
    print(hashlib.sha1(message.encode()).hexdigest())


def sha256(message):
    print(hashlib.sha256(message.encode()).hexdigest())
