import os
import re
from lib import config
from lib.fuction import show,attack

def cin():
    '''
    控制台输入函数
    '''
    # 提示用户进行输入
    if config.Pwd == '':
        msg = input("FrostBlade > ")
    else:
        msg = input("FrostBlade (" + config.Pwd +') > ')
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
    if judge == 1:
        print('[+] ' + msg + ' is running!')
    if judge == 0:
        print('[-] '+ msg + " is error in FrostBlade! You can use help to show how to use FrostBlade!")
    return

def handle(msg):
    '''
    控制台内容处理函数
    '''
    judge = 0
    # 判断用户输入到内容是否为系统命令，如果为系统命令则执行
    if judge == 0:
        for i in config.SystemCommand:
            if  i == msg:
                os.system(msg)
                judge = 1
                cout(judge,msg)
                
    # 判断用户输入内容是否为工具的命令，如果是则直接执行
    if judge == 0:
        for i in config.ToolCommand:
            if  i == msg:
                judge = 1
                cout(judge,msg)
                os.system(msg)
        
    # 判断用户输入到内容是否为图形化工具的命令，如果是则调用配置文件中的命令进行打开
    if judge == 0:
        for i in config.GraphicalTools:
            if i == msg:
                judge=1
                cout(judge,msg)     
                os.system(config.GraphicalTools[i])

    # 判断用户输入的内容是否为需要调用某些命令行工具
    if judge == 0:
        for i in config.PyTools:
            if re.match('^'+i , msg):
                msg = re.sub('^'+i,'',msg)
                judge = 1
                cout(judge,config.PyTools[i]+msg)
                os.system(config.PyTools[i]+msg)

    # 判断用户输入的内容是否是需要显示某些信息
    if re.match('^show ',msg) and judge == 0:
        tmp = msg[5:]
        if 'tools' == tmp:
            judge=1
            cout(judge,msg)
            show.show_tools()          
        elif 'pocs' == tmp:
            judge=1
            cout(judge,msg)
            show.show_pocs()
        elif 'options' == tmp:
            judge = 1
            cout(judge,msg)
            att.show_opitons()

    # 判断用户输入的内容是否是要进入的路径
    if re.match('^use ',msg) and judge == 0:
        tmp = msg[4:]
        keys = config.PocFile.keys()
        for i in keys:
            if tmp == i:
                config.Pwd = i
                judge = 1
                break
            for j in config.PocFile[i]:
                if j in tmp:
                    config.Pwd = i+'/'+j
                    judge = 1
        if judge == 1:
            att.clear_list()
            att.init()

    # 判断用户是否要会到初始目录
    if re.match('^back ',msg) and judge == 0:
        num = msg.count('..')
        pwd = config.Pwd
        pwd=pwd.split('/')
        if num == 0 or len(pwd)-num == 0:
            config.Pwd = ''
            judge = 1
        elif len(pwd)-num > 0:
            for i in range(0,len(pwd)-num):
                if i == 0:
                    config.Pwd = pwd[i]
                else:
                    config.Pwd = config.Pwd + '/' + pwd[i]
            judge = 1
        if judge == 1:
            att.clear_list() 

    # 判断用户是否要设置某些参数
    if re.match('^set ',msg) and judge == 0 and att.judge() != 0:
        tmp = msg[4:]
        tmp = tmp.split()
        if len(tmp) == 2:
            att.set_message(tmp[0],tmp[1])
            judge = 1
            cout(judge,msg)
    
    # 判断用户是否要对参数进行增加
    if re.match('^add ',msg) and judge == 0 and att.judge() != 0:
        tmp = msg[4:]
        tmp = tmp.split()
        if len(tmp) == 2:
            att.add_message(tmp[0],tmp[1])
            judge = 1
            cout(judge,msg)

    # 判断用户是否要进行攻击
    if (msg == 'exploit' or msg == 'run' ) and judge == 0 and att.judge() == 2:
        judge = 1
        att.exploit()

    # 用户输入的内容不合法，提示错误信息
    if judge == 0:
        cout(judge,msg)
    elif judge == 1:
        judge = 0

def cmd():
    '''
    控制台运行函数
    '''
    # 控制台欢迎语句
    print("\nWelcome to FrostBlade! \nYou can do everything you want in this and have a goot time!\n")
    # 循环等待用户输入，直到退出
    global att
    att = attack.pocmessage()
    while(1):
        judge_cmd=cin()
        if judge_cmd==0:
            break