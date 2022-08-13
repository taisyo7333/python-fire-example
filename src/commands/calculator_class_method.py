# -*- coding: utf-8 -*-


class Calculator(object):
    """
    A simple calculator class.
    class method version
    """

    def __init__(self) -> None:
        pass

    @classmethod
    def double(cls, number):
        """
        x * 2
        """
        return 2 * number

    @classmethod
    def triple(cls, number):
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
