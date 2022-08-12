# -*- coding: utf-8 -*-
import fire


class Calculator(object):
    """
    A simple calculator class.
    instance method version
    """

    def __init__(self):
        pass

    def double(cls, number):
        """
        x * 2
        """
        return 2 * number

    def trible(cls, number):
        """
        x * 3
        """
        return 3 * number

    def square(cls, number):
        """
        x * x
        """
        return number * number


if __name__ == '__main__':
    fire.Fire(Calculator2)
