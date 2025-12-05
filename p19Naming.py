"""
标识符（变量， 类， 方法）命名规则：
只能使用英文，数字，_, 第一个字不能用数字
大小写敏感
不可使用关键字：关键字只有： False， True，None 第一个字母是大写，其他都是小写开头
reserved names： 
False True   None    and as assert break class   
continue    def del elif    else    except  finally for
from    global  if  import  in is   lambda  nonlocal    
not or  pass    raise   return  try while   with    yield

规范：
1. 明了， 简洁 - 见明知意
2. 下划线分开两个单词
3. English Characters: all lower case
"""

name = "Sherri"
_name = "Sherri"
name_ = "Liang" 

itheima = "black horse"
Itheima = 666
print(itheima)  # black horse
print(Itheima)  # 666