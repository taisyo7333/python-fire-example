# -*- coding: utf-8 -*-


class Calculator(object):
    """
    A simple calculator class.
    instance method version
    """

    def __init__(self) -> None:
        pass

    def double(self, number):
        """
        x * 2
        """
        return 2 * number

    def triple(self, number):
        """
        x * 3
        """
        return 3 * number

    def square(self, number):
        """
        x * x
        """
        return number * number
