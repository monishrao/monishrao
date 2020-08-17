import random
import inspect
import decimal
import math
from math import sqrt
from decimal import Decimal
from datetime import datetime


def time_it(fn, *args, repetitions=1, **kwargs):


    if not ((type(repetitions)==int)  and (repetitions>=0)):
        raise ValueError("invalid value: repetitions should be integer and >0")

    start = datetime.now()




    if not (len([*args,*kwargs]) ==  fn.__code__.co_argcount):
        raise TypeError("invalid arguments: arguments passed are not valid for function called")


    for i in range(repetitions):
        fn(*args, **kwargs)

    end = datetime.now()

    avg_time = ((end - start).total_seconds()) / repetitions
    return avg_time

def squared_power_list(num,start=0,end=5):


    if (type(start)!=int or type(end)!=int):
        raise ValueError("invalid value: start and end can only be int")

    sq_pow_list=[]

    if not (start < end):
        start,end = end,start
        for i in range(start,end+1):
            sq_pow_list.append(num**i)
        sq_pow_list.reverse()
    else:
        for i in range(start,end+1):
            sq_pow_list.append(num**i)

    print(sq_pow_list)
    return sq_pow_list

def polygon_area(a,sides = 3):

    if not ((type(sides)==int)  and (3 <= sides <= 6)):
        raise ValueError("invalid value: sides should be integer and between 3 and 6 both inclusive")

    if not ((type(a)==int or type(a)==float)):
        raise ValueError("invalid value: length should be int or float")

    if not (a>0):
        raise ValueError("invalid value: length should be positive number")

    if sides==3:
        area = sqrt(3) * (a**2)/4
    elif sides==4:
        area = (a**2)
    elif sides==5:
        area = sqrt(5*(5 + 2*sqrt(5)))  * (a**2)/4
    elif sides==6:
        area= 3 * sqrt(3) * (a**2)/2

    print(area)
    return area


def temp_converter(base_temp, temp_given_in='f'):



    if not (temp_given_in in ['f', 'c']):
        raise ValueError("invalid value: temp_given_in should be either 'c' or 'f'")

    if not ((type(base_temp)==int or type(base_temp)==float)):
        raise ValueError("invalid value: base_temp should be int or float")

    if temp_given_in == 'f':
        temp_converted = (base_temp - 32) * 5 / 9
    elif temp_given_in == 'c':
        temp_converted = (base_temp * 9 / 5) + 32

    print(temp_converted, set(['f', 'c']) - set(temp_given_in))
    return temp_converted


def speed_converter(base_speed, dist='km', time='hr'):



    if not (dist in ['km', 'm', 'ft', 'yrd']):
        raise ValueError("invalid value: dist should be one of ['km','m','ft','yrd'] ")

    if not (time in ['ms', 's', 'min', 'hr', 'day']):
        raise ValueError("invalid value: time should be one of ['ms','s','min','hr','day'] ")

    if not ((type(base_speed)==int or type(base_speed)==float)):
        raise ValueError("invalid value: base_temp should be int or float")

    if not (base_speed>=0):
        raise ValueError("invalid value: base_speed should be positive number")

    dist_dict = {'km': 1, 'm': 1000, 'ft': 3280.84, 'yrd': 1093.61}
    time_dict = {'ms': 3600000, 's': 3600, 'min': 60, 'hr': 1, 'day': 1.0 / 24}
    speed_converted = base_speed * dist_dict[dist] / time_dict[time]

    print(speed_converted, dist + '/' + time)

    return speed_converted





