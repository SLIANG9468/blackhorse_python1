'''
黑马程序员python零基础全程教程， 8 天python从入门到精通，学python看这套就够了
 for blackhorse_python1
 字面量：   literal
'''
# p17 查看数据类型

print("money has:", 50)
print(type("黑马程序员"))
print(type(666))
print(type(13.14))

string_type = type("black horse")
int_type = type(666)
float_type = type(11.345)
print(string_type)  # <class 'str'>
print(int_type)     # <class 'int'>
print(float_type)   #<class 'float'>

# use type to check the type of variable

name = "black horse"
name_type = type(name)
print(name_type)    # <class 'str'>