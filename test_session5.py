import pytest
import random
import string
import session5
import os
import inspect
import re
import math
from math import isclose
import decimal


README_CONTENT_CHECK_FOR = [
    'time_it',
    'print',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()

    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():

    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_invalid_time_it_valueerror():
    with pytest.raises(ValueError):
        session5.time_it(session5.speed_converter,100,dist='m',time='s',repetitions=-1)
    with pytest.raises(ValueError):
        session5.time_it(session5.speed_converter,100,dist='m',time='s',repetitions=5.5)
    with pytest.raises(ValueError):
        session5.time_it(session5.speed_converter,100,dist='m',time='s',repetitions='a')

def test_invalid_time_it_typeerror():
    with pytest.raises(TypeError):
        session5.time_it(session5.speed_converter,100,repetitions=1)

def test_invalid_time_it_wrongarguments():
    with pytest.raises(TypeError):
        session5.time_it(session5.speed_converter,100,sides=3,time='s',repetitions=1)
    with pytest.raises(TypeError):
        session5.time_it(session5.squared_power_list,2, start1=1, end=10, repetitions=5)

def test_time_it_squared_power_list():
    assert session5.time_it(session5.squared_power_list,2, start=1, end=10, repetitions=500) <0.1,'function not proper'

def test_time_it_polygon_area():
    assert session5.time_it(session5.polygon_area,15, sides = 3, repetitions=500) <0.1,'function not proper'

def test_time_it_temp_converter():
    assert session5.time_it(session5.temp_converter,100, temp_given_in = 'c', repetitions=200) <0.1,'function not proper'

def test_time_it_speed_converter_time():
    assert session5.time_it(session5.speed_converter,100,dist='m',time='s',repetitions=500) <0.1,'function not proper'

def test_invalid_squared_power_list_valueerror():
    with pytest.raises(ValueError):
        session5.squared_power_list(10, -1, 'abc')
    with pytest.raises(ValueError):
        session5.squared_power_list(10, 'abc', 2)

def test_squared_power_list():
    assert session5.squared_power_list(2,start=0,end=5) == [1,2,4,8,16,32], 'function not working properly'

def test_squared_power_list_reverse():
    assert session5.squared_power_list(2,start=5,end=0) == [32,16,8,4,2,1], 'function not working properly'

def test_squared_power_list_negative():
    assert session5.squared_power_list(2,start=1,end=-1) == [2,1,0.5], 'function not working properly'

def test_invalid_polygon_area_valueerror():
    with pytest.raises(ValueError):
        session5.polygon_area(10, -1)
    with pytest.raises(ValueError):
        session5.polygon_area('abc', 5)
    with pytest.raises(ValueError):
        session5.polygon_area(-10, 5)

def test_polygon_area_triangle():
    assert session5.polygon_area(15,3) == 97.42785792574934, 'function not working properly'

def test_polygon_area_square():
    assert session5.polygon_area(15,4) == 225, 'function not working properly'

def test_polygon_area_pentagon():
    assert session5.polygon_area(15,5) == 387.10741513251753, 'function not working properly'

def test_polygon_area_hexagon():
    assert session5.polygon_area(15,6) == 584.5671475544962, 'function not working properly'

def test_invalid_temp_converter_valueerror():
    with pytest.raises(ValueError):
        session5.temp_converter(10, 'd')
    with pytest.raises(ValueError):
        session5.temp_converter('abc', 'c')

def test_temp_converter_celsius_to_f():
    assert session5.temp_converter(100,'c') == 212.0, 'function not working properly'

def test_temp_converter_f_to_celsius():
    assert session5.temp_converter(212,'f') == 100.0, 'function not working properly'

def test_invalid_speed_converter_valueerror():
    with pytest.raises(ValueError):
        session5.speed_converter(10, dist='d',time='s')
    with pytest.raises(ValueError):
        session5.speed_converter(10, dist='km',time='year')
    with pytest.raises(ValueError):
        session5.speed_converter('abc', dist='km',time='min')
    with pytest.raises(ValueError):
        session5.speed_converter(-10, dist='km',time='min')

def test_speed_converter_kmph_to_mpsec():
    assert session5.speed_converter(100,dist='m',time='s') == 27.77777777777778, 'function not working properly'

def test_speed_converter_kmph_to_yrdpsec():
    assert session5.speed_converter(100,dist='yrd',time='s') == 30.37805555555555, 'function not working properly'

def test_speed_converter_kmph_to_kmpday():
    assert session5.speed_converter(100,dist='km',time='day') == 2400.0, 'function not working properly'

def test_speed_converter_kmph_to_ftpms():
    assert session5.speed_converter(100,dist='ft',time='ms') == 0.09113444444444445, 'function not working properly'

