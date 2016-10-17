#!/usr/bin/env python
import sys


def factorial(n):
    if n < 0:
        raise Exception('Unable to calculate factorial of negative number')
    if n <= 1:
        return n
    return n * factorial(n-1)


def main():
    print('Hello, world!')
    return 0

if __name__ == '__main__':
    sys.exit(main())
