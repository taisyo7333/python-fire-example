# -*- coding: utf-8 -*-
import os


def hello(name="world") -> str:
    """
    hello world
    """
    return "Hello %s!" % name


def get_env(key="ENV", default="") -> str:
    """
    get environment
    """
    return os.environ.get(key, default)
