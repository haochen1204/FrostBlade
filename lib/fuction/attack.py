import importlib
import threading
import re
from lib import config
from lib.fuction import file

class attack:

    def __init__(self,poc_pwd):
        '''
            设置要使用的poc
        '''
        self.pwd = poc_pwd
        self.pwd=self.pwd.replace('/','.')
        self.pwd=self.pwd.replace('.py','')
        self.poc = importlib.import_module(self.pwd).POC()
        self.parameter=self.poc.parameter

    def show_msg(self):
        '''
            展示特定漏洞信息的函数
        '''
        keys = self.parameter.keys()
        for i in keys:
            if i != 'target':
               print("     {0:^10}     {1:5}      {2:<20}".format(i,'YES',self.parameter[i])) 
        self.poc.show_options()

    def exploit(self):
        '''
            运行poc进行攻击或者扫描
        '''
        #print(self.poc.poc_pwd)
        if 'scanner' in self.pwd:
            self.poc.scanner(self.parameter)
        elif 'exploit' in self.pwd:
            self.poc.exploit(self.parameter)


class pocmessage:

    thread = 1 # 运行的线程数
    target_pwd = '' # 被攻击目标的目录
    target_list = [] # 被攻击的目标的列表
    poc_pwd = '' # 使用的poc存在的目录
    poc_list = [] # 使用的poc的列表
    parameter = {
        'target' : ''
    }

    def init(self):
        '''
            类的初始化函数
        '''
        self.poc_pwd = config.Pwd
        keys = config.PocFile.keys()
        if re.search('.py$',self.poc_pwd):
            # 如果以.py结尾，证明只使用了一个poc，需要显示这个poc的详细信息，所以将其实例化
            self.poc_list.append(self.poc_pwd)
            self.att = attack(self.poc_pwd)
            # 获取该poc需要的参数
            self.parameter = self.att.parameter
        else:
            for i in keys:
                if re.match('^'+self.poc_pwd,i) and 'exploit' not in i:
                    for j in config.PocFile[i]:
                        self.poc_list.append(i + '/' + j)

    def judge(self):
        '''
            判断攻击函数中的参数是否设置完成
        '''
        # 判断参数是否设置完成
        judge = 0
        keys = self.parameter.keys()
        for i in keys:
            if i != 'target':
                if self.parameter[i] == '':
                    judge = 1
        if len(self.target_list) == 0 and len(self.poc_list) == 0:
            return 0 # 没有进行任何设置
        elif len(self.poc_list) > 0 and len(self.target_list) == 0:
            return 1 # 未设置poc
        elif len(self.poc_list) > 0 and len(self.target_list) > 0 and judge == 0:
            return 2 #设置完成

    def show_opitons(self):
        '''
            展示需要设置的信息
        '''
        print('')
        print("     {0:^10}     {1:5}      {2:<20}".format('Thread','NO',self.thread))
        print("     {0:^10}     {1:5}      {2:<20}".format('Target','YES',self.target_pwd))
        # 判断是否有多个被攻击目标
        if len(self.target_list) > 0:
            for i in self.target_list:
                if i != ' ':
                    print("     {0:^10}     {1:5}      {2:<20}".format('','',i))
        print("     {0:^10}     {1:5}      {2:<20}".format('POC','YES',self.poc_pwd))
        # 判断使用的poc数量，如果只使用了一个poc，那么显示poc的详细信息
        if self.poc_pwd not in self.poc_list:
            for i in self.poc_list:
                if i !=' ':
                    print("     {0:^10}     {1:5}      {2:<20}".format('','',i)) 
        else:
            print('')
            self.att.show_msg()
            print('')


    def add_message(self,msg,input):
        '''
            用户增加poc或者target的函数
        '''
        if msg == 'target':
            self.target_list.append(input)
        if msg == 'poc':
            self.poc_list.append(input)
    
    def set_message(self,msg,input):
        '''
            用户设置攻击信息的函数
        '''
        keys = self.parameter.keys()
        if msg == 'target':
            self.target_pwd = input
            self.__read_file()
        elif msg == 'thread':
            self.thread = int(input)
        elif msg in keys:
            self.parameter[msg] = input

    def __read_file(self):
        '''
            根据文件内容设置目标
        '''
        self.target_list = file.read_file_line(self.target_pwd)

    def clear_list(self):
        '''
            一次运行结束后清空内容，为下次运行做准备
        '''
        self.target_list.clear()
        self.poc_list.clear()
        self.thread = 1
        self.poc_pwd = ''
        self.target_pwd = ''
        self.parameter = {
            'target' : ''
        }

    def exploit(self):
        '''
            调用攻击类使用的函数
        '''
        poc_num = 0
        target_num = 0
        poc_max = len(self.poc_list)
        target_max = len(self.target_list)
        #print(str(poc_max)+'***'+str(target_max))
        print('')
        print('target : ' +str(target_max)+'  poc : '+ str(poc_max)+ ' total : '+str(poc_max*target_max)+'\n')
        print('    {0:^10}  {1:^50} {2:^20}'.format('status','target','pocname'))
        if self.judge() == 2:
            while True:
                if threading.active_count()-1 <= self.thread:
                    #print(str(threading.active_count()))
                    if target_num < target_max:
                        #print("("+str(threading.active_count())+")")
                        #print(str(poc_num)+'******'+str(target_num))
                        att = attack(self.poc_list[poc_num])
                        att.parameter=self.parameter
                        att.parameter['target']=self.target_list[target_num]
                        thread = threading.Thread(target=att.exploit)
                        thread.start()
                        poc_num = poc_num + 1
                        if poc_num == poc_max:
                            poc_num = 0
                            target_num = target_num + 1
                    else:
                        if threading.active_count() == 1:
                            print('')
                            break
        else:
            print('\n请设置需要的参数！\n')
