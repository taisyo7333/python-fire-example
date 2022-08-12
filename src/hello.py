# -*- coding: utf-8 -*-
import fire

def hello(name="world"):
    """
    hello world
    """
    return "Hello %s!" % name


if __name__ == '__main__':
    fire.Fire(hello)
