def is_divided(prime_list, num):
    for prime in prime_list:
        if num % prime == 0:
            return True
        return False


def main():
    li1 = list(range(5, 1000, 2))
    primes = [2, 3]
    for i in li1:
        if not is_divided(primes, i):
            primes.append(i)

    print('η διαφορα μεταξυ του μικροτερου και του μεγαλυτερου πρωτου ειναι ', primes[-1] - primes[0])


if __name__ == '__main__':
    main()


