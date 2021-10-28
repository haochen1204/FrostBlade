from re import I
from lib import file
from lib import output
import lib
import importlib
import threading
import os


class attack:

    def __init__(self,poc_pwd):
        '''
            设置要使用的poc
        '''
        # 定义区域
        self.output = output.cmd_output()
        # poc class的列表
        self.poc_list = []
        # poc 参数信息的列表
        self.must_parameter_list = []
        self.choo_parameter_list = []
        self.must_parameter = {
            'target' : ''
        }
        self.choo_parameter = {
            'thread' : '30'
        }
        # 处理区域
        self.pwd = poc_pwd
        self.pocs_pwd = file.file().search_pocs(self.pwd)
        # 循环获取poc并创建对应的类，加入到列表当中
        for i in self.pocs_pwd:
            i=i.replace('/','.')
            i=i.replace('.py','') 
            tmp_poc = importlib.import_module(i).POC()
            self.poc_list.append(tmp_poc)
            self.must_parameter_list.append(tmp_poc.must_parameter)
            self.choo_parameter_list.append(tmp_poc.choo_parameter)
        # 循环读取所需要的参数，并整理到must_parameter当中
        for i in self.must_parameter_list:
            for j in i.keys():
                if j not in self.must_parameter.keys():
                    if i[j] != '':
                        self.must_parameter[j] = i[j]
                    else:
                        self.must_parameter[j]=''
        for i in self.choo_parameter_list:
            for j in i.keys():
                if j not in self.choo_parameter.keys():
                    if i[j] != '':
                        self.choo_parameter[j] = i[j]
                    else:
                        self.choo_parameter[j]=''

    def judge(self):
        '''
            判断所要设置的参数是否设置完成
        '''
        keys = self.must_parameter.keys()
        for i in keys:
            if self.must_parameter[i] == '':
                return False
        return True

    def get_info(self):
        '''
            获取poc基础信息的函数
        '''
        msg = []
        for i in self.poc_list:
            msg.append(i.get_info())
        return msg

    def get_parameter(self):
        '''
            获取poc参数信息的函数
        '''
        msg = []
        for i in self.must_parameter.keys():
            tmp_msg = []
            tmp_msg.append(i)
            tmp_msg.append('YES')
            tmp_msg.append(str(self.must_parameter[i]))
            msg.append(tmp_msg)
        for i in self.choo_parameter.keys():
            tmp_msg = []
            tmp_msg.append(i)
            tmp_msg.append('NO')
            tmp_msg.append(str(self.choo_parameter[i]))
            msg.append(tmp_msg)
        return msg
    
    def run(self):
        '''
            开始运行的函数
        '''
        target_list = []
        if os.path.exists(self.must_parameter['target']):
            target_list = file.file().read_file(self.must_parameter['target'])
        else:
            target_list.append(self.must_parameter['target'])
        thread_max = int(self.choo_parameter['thread'])
        target_max_index = len(target_list)
        poc_max_index = len(self.poc_list)
        poc_index = 0
        target_index = 0
        print('target:'+str(target_max_index))
        print('poc:'+str(poc_max_index))
        print(str(target_list))
        print(str(self.poc_list))
        while True:
            if threading.active_count() - 1 < thread_max and poc_index < poc_max_index:
                tmp_must_parameter = self.must_parameter
                tmp_choo_parameter = self.choo_parameter
                tmp_must_parameter['target'] = target_list[target_index]
                th = threading.Thread(target=self.poc_list[poc_index].exploit,args=(tmp_must_parameter,tmp_choo_parameter))
                th.start()
                target_index += 1
                if target_index >= target_max_index:
                    target_index = 0
                    poc_index += 1
            if poc_index >= poc_max_index and threading.active_count() == 1:
                self.output.output_attack(lib.POC_MESSAGE,'poc result')
                lib.POC_MESSAGE = []
                break
