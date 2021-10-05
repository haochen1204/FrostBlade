import os
from lib import config

def cin():
    '''
    控制台输入函数
    '''
    # 提示用户进行输入
    msg = input("FrostBlade > ")
    # 如果输入为exit，则打印再见语句，并退出命令行，否则继续运行循环
    if msg == "exit":
        print("See you!\n")
        return False
    else:
        handle(msg)
    return True

def cout():
    '''
    控制台输出函数
    '''
    return

def handle(msg):
    '''
    控制台内容处理函数
    '''
    # 判断用户输入到内容是否为系统命令，如果为系统命令则执行
    for i in config.SystemCommand:
        if i in msg:
            os.system(msg)
    # 判断用户输入内容是否为工具的命令，如果是则直接执行
    for i in config.ToolVersion:
        if i in msg:
            os.system(msg)
    print(msg)
    return

def cmd():
    '''
    控制台运行函数
    '''
    # 控制台欢迎语句
    print("\nWelcome to FrostBlade! \nYou can do everything you want in this and have a goot time!\n")
    # 循环等待用户输入，直到退出
    while(True):
        judge=cin()
        if judge==False:
            break