
def cin():
    '''
    控制台输入函数
    '''

    msg = input("HcPoc > ")
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
    print(msg)
    return

def cmd():
    '''
    控制台运行函数
    '''
    print("\nWelcome to HcPoc! \nYou can do everything you want in this and have a goot time!\n")
    while(True):
        judge=cin()
        if judge==False:
            break
    return