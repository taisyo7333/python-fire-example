# -*- coding: utf-8 -*-
import fire


class Calculator(object):
    """
    A simple calculator class.
    class method version
    """

    def __init__(self):
        pass

    @classmethod
    def double(cls, number):
        """
        x * 2
        """
        return 2 * number

    @classmethod
    def trible(cls, number):
        """
        x * 3
        """
        return 3 * number

    @classmethod
    def square(cls, number):
        """
        x * x
        """
        return number * number


if __name__ == '__main__':
    fire.Fire(Calculator)
