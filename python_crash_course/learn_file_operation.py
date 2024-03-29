# -*- coding:utf-8 -*-
# 《python编程：从入门到实践》第10章 文件和异常
# 学习处理文件，并处理异常
from os import close
import os
import json

filename = '../src/test.txt'

# 读取文件
# 路径，在windows中用反斜杠，在linux和OS x中用斜杠
with open(filename) as file_object:  # open()打开文件
    # with可以在访问文件之后关闭它，也可以用open()和close()，但是只会在close时才关闭，如果调试未执行到close，会导致文件未妥善处理
    # open()仅在with代码块中使用，如果要给别的地方用，存储下来
    contents = file_object.read()
    print(contents.rstrip())  # .rstrip()用于删除末尾的空白
# 打印到一行中
message_string = ''
for line in contents:  # 此处已被关闭，无法读取内容，
    message_string += line.strip()  # 相较rstrip，strip可以去除前面的空格
m_replace = message_string.replace('i', 'I')  # 并不会真正替换
print(message_string)
print(m_replace)
print(len(message_string))  # 长度

new_file = open(filename)
contents = new_file.read()
print(contents.rstrip())  # .rstrip()用于删除末尾的空白
# 打印每一行
for line in file_object:
    print(line)
close(filename)

# 写文件
# 可指定读取模式 （'r' ）、写入模式 （'w' ）、附加模式 （'a' ）或让你能够读取和写入文件的模式（'r+' ）
"""
如果你省略了模式实参，Python将以默认的只读模式打开文件。
如果你要写入的文件不存在，函数open() 将自动创建它。
然而，以写入（'w' ）模式打开文件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件。
"""
filename2 = 'test.txt'
with open(filename2, 'w') as file_object:
    file_object.write("I love programming.")

# 写入多行
with open(filename2, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 附加到文件
with open(filename2, 'a') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 异常返回 try-except代码块
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# 除法计算器
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input('\nSecond number:')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(f"Answer is {answer}")

# 分析文本，文本中字数量
filename3 = 'test.txt'

try:
    with open(filename3) as file3_object:
        contents = file3_object.read()
except FileNotFoundError:
    # pass # 使用pass告诉程序什么都不做，继续向后执行
    msg = "Sorry, the file " + "does not exist."
    print(msg)
else:
    # 计算文件大概包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + "has about " + str(num_words) + "words.")


# 两个数字相加，当录入的是文本时，输出异常
def add(a: int, b: int, sum1=None):
    """加法计算器"""
    try:
        sum1 = int(a) + int(b)
    except ValueError:
        msg = "加数类型错误，请修改后尝试！"
        print(msg)
    else:
        print(f"计算结果是{sum1}")
    return sum1


while True:
    print("加法计算器，按'q'退出")
    a = input("请输入第一个加数：")
    if a == 'q':
        break
    b = input("请输入第二个加数：")
    if b == 'q':
        break
    add(a, b)

# remember_me.py
# 学习json
import json

filename4 = 'username.json'
try:
    with open(filename4) as f_obj4:
        username = json.load(f_obj4)
except FileNotFoundError:
    username = input("What is your name?")
    with open(filename4, 'w') as f_obj4:
        json.dump(username, f_obj4)
        print("We'll remember you when you come back, " + username + "!")
else:
    print(f"Welcome back, {username}!")