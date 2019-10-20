import hashlib
import random
import string
import time

from zestama import mysum


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def try_sha(n=100):
    li = []
    for i in range(n):
        s = randomString(10)
        print(s)
        current = hashlib.sha256(s.encode()).hexdigest()
        a = 0
        while not (current.startswith('a3') and current.endswith('fff')):
            current = hashlib.sha256(current.encode()).hexdigest()
            a += 1
        li.append(a)
    return li


def main():
    li = try_sha(10)
    mesos_oros = mysum(li) / 10
    print(mesos_oros)


if __name__ == '__main__':
    random.seed()
    main()
