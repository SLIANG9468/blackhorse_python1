"""
p18 数据类型转换
"""
num_str = str(11)
print(type(num_str), num_str)

float_str = str(11.12)
print(type(float_str), float_str)

num = int("11")
print(type(num), num)

num2 = float("13.14")
print(type(num2), num2)

float_num = float(11)
print(type(float_num), float_num)   # <class 'float'> 11.0

int_num = int(5.67)
print(type(int_num), int_num)   # <class 'int> 5  lost the digits after .
