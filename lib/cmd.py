import os
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
    else:
        print('[-] '+ msg)

def handle(msg):
    '''
    控制台内容处理函数
    '''
    back_msg = '请输入正确的命令'
    tmp = msg.split()
    # 判断用户输入到内容是否为系统命令，如果为系统命令则执行
    if tmp[0] in config.SystemCommand:
        cout(1,msg)
        os.system(msg)
    # 判断用户输入内容是否为工具的命令，如果是则直接执行
    elif tmp[0] in config.ToolCommand:
        cout(1,msg)
        os.system(msg)
    # 判断用户输入到内容是否为图形化工具的命令，如果是则调用配置文件中的命令进行打开
    elif tmp[0] in config.GraphicalTools.keys():
        cout(1,msg)
        os.system(config.GraphicalTools[tmp[0]])
    # 判断用户输入的内容是否为需要调用某些命令行工具
    elif tmp[0] in config.PyTools.keys():
        msg = msg.replace(tmp[0],config.PyTools[tmp[0]])
        cout(1,msg)
        os.system(msg)
    # 判断用户输入的内容是否是需要显示某些信息
    elif tmp[0] == 'show' :
        if len(tmp) != 2:
            # 参数过多的情况
            back_msg = '请输入正确数量的参数'
        else:
            if tmp[1] == 'tools':
                cout(1,msg)
                show.show_tools()
            elif tmp[1] == 'pocs':
                cout(1,msg)
                show.show_pocs()
            elif tmp[1] == 'options':
                cout(1,msg)
                att.show_opitons()
            else:
                back_msg = '参数输入错误！'
    # 判断用户是否要进入某个目录
    elif tmp[0] == 'use':
        if len(tmp) != 2:
            back_msg = '请输入正确数目的参数'
        else:
            tmp_pwd = config.Pwd
            keys = config.PocFile.keys()
            if tmp[1] in keys:
                config.Pwd = tmp[1]
                att.clear_list()
                att.init()
            else:
                for i in keys:
                    for j in config.PocFile[i]:
                        if i + '/' + j == tmp[1]:
                            config.Pwd = tmp[1]
                            att.clear_list()
                            att.init()
                            break
            if tmp_pwd == config.Pwd:
                back_msg = '路径输入错误，请重新输入！'
    # 判断用户是否要返回某个目录
    elif tmp[0] == 'break':
        num = msg.count('..')
        pwd = config.Pwd
        pwd = pwd.split('/')
        if num == 0 or len(pwd)-num == 0:
            config.Pwd = ''
            att.clear_list()
        elif len(pwd)-num > 0:
            for i in range(0,len(pwd)-num):
                if i == 0:
                    config.Pwd = pwd[i]
                else:
                    config.Pwd = config.Pwd + '/' + pwd[i]
            att.clear_list()
        else:
            back_msg = '返回路径错误！'
    # 判断用户是否要设置某些参数
    elif tmp[0] == 'set':
        if config.Pwd != 'pocs' and att.judge() != 0:
            if len(tmp) != 3:
                back_msg = '请输入正确数目的参数'
            else:
                judge = att.set_message(tmp[1],tmp[2])
                if judge == True:
                    cout(1,msg)
                else:
                    back_msg = tmp[1] + '参数不存在！'
        else:
            back_msg='请先设置攻击使用的poc'
    # 判断用户是否要增加某些参数
    elif tmp[0] == 'add':
        if config.Pwd!= 'pocs' and att.judge() != 0:
            if len(tmp) != 3:
                back_msg = '请输入正确数目的参数'
            else:
                judge = att.add_message(tmp[1],tmp[2])
                if judge == True:
                    cout(1,msg)
                else:
                    back_msg = tmp[1] + '参数不存在！'
        else:
            back_msg= '请先设置攻击使用的poc'
    # 判断用户是否要进行攻击
    elif tmp[0] == 'exploit' or tmp[0] == 'run':
        if att.judge() == 2:
            att.exploit()
        else:
            back_msg = '请先完成对参数的设置'
    else:
        cout(0,back_msg)
    if back_msg != '请输入正确的命令':
        cout(0,back_msg)

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