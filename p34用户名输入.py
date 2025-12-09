"""
https://www.bilibili.com/video/BV1sHU9BmEne?spm_id_from=333.788.player.switch&vd_source=f91c72f5e6c586dc724d0e8738d874e8&p=34
Valid users: admin/1234; zhang/5678; chen/abc
if either username or pwd is empty, error message and input again
if either username or pwd is not correct, error message and input again
only allow 5 times input
"""
for i in range(5):
    username = input("Please type username: ")
    pwd = input("Please type password: ")
    if username == '' or pwd == '':
        print('username or pwd can\'t be empty')
        continue

    if username == 'admin' and pwd == '1234':
        print("welcome")
        break
    elif username == 'zhang' and pwd == '5678':
        print("Welcome")
        break
    elif username == 'chen' and pwd == 'abc':
        print("Welcome")
        break
    else:
        print("Username or Pwd is not correct")



