import datetime
from genericpath import exists
import lib
import os
from lib import color
from prettytable import PrettyTable

class cmd_output:

    def __init__(self):
        '''
            初始化
        '''
        self.color = color.Colored()
        self.tb = PrettyTable()

    def __clear_tb(self):
        '''
            清除表格中的数据
        '''
        self.tb.clear()

    def get_time(self):
        '''
            获取当前时间
        '''
        now_time = datetime.datetime.now().strftime('%H:%M:%S')
        now_time = '['+now_time+'] '
        now_time = self.color.cyan(now_time)
        return now_time 

    def output_error(self,msg,feed=False):
        '''
            输出错误信息
        '''
        if feed == True:
            now_time = '\n'+self.get_time()
        else:
            now_time = self.get_time()
        
        
        print(now_time+self.color.red('[ERROR] ')+msg)

    def output_warning(self,msg,feed=False):
        '''
            输出警告信息
        '''
        if feed == True:
            now_time = '\n'+self.get_time()
        else:
            now_time = self.get_time()
        print(now_time+self.color.yellow('[WARNING] ')+msg)
    
    def output_info(self,msg,feed=False):
        '''
            输出提示信息
        '''
        if feed == True:
            now_time = '\n'+self.get_time()
        else:
            now_time = self.get_time()
        print(now_time+self.color.green('[INFO] ')+msg)

    def output_message(self,msg,head=''):
        '''
            输出信息
        '''
        if head != '':
            self.output_info(head + ' message:',False)
            self.tb.field_names = lib.FIELD_NAMES[head]
        self.tb.add_rows(msg)
        print(self.tb)
        self.__clear_tb()

    def output_attack(self,msg,head='',sort=''):
        '''
            输出攻击结果
        '''
        if head != '':
            self.output_info(head + ' message:',False)
            self.tb.field_names = lib.FIELD_NAMES[head]
        msg = self.__heandle_message_color(msg)
        self.tb.add_rows(msg)
        if sort == '':
            print(self.tb)
        else:
            print(self.tb.get_string(sortby=sort.upper()))
        self.__clear_tb()

    def __heandle_message_color(self,msg):
        '''
            根据内容处理应该输出的颜色
        '''
        tmp = []
        for i in msg:
            if 'success' in i:
                i = self.color.green_list(i)
            elif 'error' in i:
                i = self.color.red_list(i)
            elif 'failed' in i:
                i = self.color.yellow_list(i)
            tmp.append(i)
        return tmp

    def output_file(self,path,msg):
        try:
            f = open(path,'w+')
        except:
            self.output_error('文件路径错误，导出结果到文件失败！')
        if os.path.getsize(path) != 0:
            self.__clear_file(path)
        for i in msg:
            for j in i:
                f.write(j+' ')
            f.write('\n')
        

    def __clear_file(self,path):
        with open(path, "r+") as f:
            read_data = f.read()
            f.seek(0)
            f.truncate()

