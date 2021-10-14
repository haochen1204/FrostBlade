import os
import re
from lib import config
from lib.fuction import show

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

def cout(judge,msg):
    '''
    控制台输出函数
    '''
    if judge == True:
        print('[+] ' + msg + ' is running!')
    if judge == False:
        print('[-] '+ msg + " is not used in FrostBlade! You can use help to show how to use FrostBlade!")

    return

def handle(msg):
    '''
    控制台内容处理函数
    '''
    # 判断命令是否执行成功用
    judge = False

    # 判断用户输入到内容是否为系统命令，如果为系统命令则执行
    for i in config.SystemCommand:
        if  i == msg:
            cout(judge,msg)
            os.system(msg)
            judge = True
            
    # 判断用户输入内容是否为工具的命令，如果是则直接执行
    if judge == False:
        for i in config.ToolCommand:
            if  i == msg:
                judge = True
                cout(judge,msg)
                os.system(msg)
      
    # 判断用户输入到内容是否为图形化工具的命令，如果是则调用配置文件中的命令进行打开
    if judge == False:
        for i in config.GraphicalTools:
            if i == msg:
                judge=True
                cout(judge,msg)     
                os.system(config.GraphicalTools[i])

    # 判断用户输入的内容是否为需要调用某些命令行工具
    if judge == False:
        for i in config.PyTools:
            if re.match('^'+i , msg):
                msg = re.sub('^'+i,'',msg)
                judge = True
                cout(judge,config.PyTools[i]+msg)
                os.system(config.PyTools[i]+msg)

    # 判断用户输入的内容是否是需要显示某些信息
    if re.match('^show ',msg) and judge == False:
        tmp = msg[5:]
        if 'tools' == tmp:
            judge=True
            cout(judge,msg)
            show.show_tools()          
        elif 'pocs' == tmp:
            judge=True
            cout(judge,msg)
            show.show_pocs()

    # 用户输入的内容不合法，提示错误信息
    if judge == False:
        cout(judge,msg)

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