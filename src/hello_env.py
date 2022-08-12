# -*- coding: utf-8 -*-
import fire
import os

def get_env(key="ENV",default=""):
    """
    get environment
    """
    return os.environ.get(key,default)

if __name__ == '__main__':
    fire.Fire(get_env)
