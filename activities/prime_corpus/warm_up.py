from glob import glob

from nltk import word_tokenize


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):   # only odd numbers
        if n % i == 0:
            return False
    return True


def is_prime_slow(n):
    """Simple, but slow, implementation."""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    test = int(input('Enter a number to see if it is prime: '))
    if is_prime(test):
        print(f'{test} is prime!')
    else:
        print(f"{test} is not prime, but I'm sure you're a good person.")
    print('Iterating over files in this directory...')
    for each in sorted(glob('*.txt')):
        with open(each) as the_file:
            if is_prime_slow(len(word_tokenize(the_file.read()))):
                print(each)
