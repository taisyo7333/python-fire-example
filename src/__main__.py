import os

import fire

from commands import calculator_class_method as calc_cm
from commands import calculator_instance_method as calc_im
from commands.hello import get_env, hello

if __name__ == "__main__":
    fire.Fire(
        {
            "hello": hello,
            "calc-class": calc_cm.Calculator,
            "calc-instance": calc_im.Calculator,
            "os": os,
            "env": get_env,
        }
    )
