import fire
import os

import calculator_class_method as calc_cm
import calculator_instance_method as calc_im
import hello
import hello_env

if __name__ == '__main__':
    fire.Fire({
        'hello': hello.hello,
        'calc-class': calc_cm.Calculator,
        'calc-instance': calc_im.Calculator,
        'os': os,
        'env': hello_env,
        })
