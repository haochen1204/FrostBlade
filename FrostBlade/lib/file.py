import os
from lib import output

class file:

    def __init__(self):
        self.__output = output.cmd_output()
        # 获取上级路径
        self.__now_path = os.path.dirname(os.path.dirname(__file__))
        # poc文件的绝对路径
        self.__poc_path = ''
        # pocs的路径
        self.pocs = []
        # pocs的目录
        self.pocs_list = []
        # modules的绝对路径
        self.__modules_path = ''
        # modules的路径
        self.modules = []

    def read_pocs(self):
        '''
            读取存在的poc及其信息
        '''
        # 获取poc路径
        try:
            self.__poc_path = os.path.join(self.__now_path,'pocs')
        except:
            self.__output.output_error('无法正确获取poc路径，请检查文件是否完整！',False)
        # 获取所有的poc
        index = 0
        for root, dirs, files in os.walk(self.__poc_path):
            if '__pycache__' not in root:
                # 将poc目录假如到pocs_list中（仅限于poc目录，不加入exp目录）
                tmp = 'FrostBlade' + os.sep
                tmp_path = root.split(tmp)[2]
                if 'scanner' in tmp_path:
                    self.pocs_list.append(tmp_path)
                # 将文件加入到pocs中
                for i in files:
                    if i != '__init__.py':
                        # 将绝对路径修改为相对路径
                        # 绝对路径
                        tmp_poc_path = root + os.sep + i
                        # 相对路径
                        tmp_path = tmp_poc_path.split(tmp)[2]
                        # 读取文件信息
                        msg = '无poc名称信息，请检查poc'
                        try:
                            f = open(tmp_poc_path,'r',encoding='UTF-8')
                        except:
                            self.__output.output_error('无法正确打开poc，请检查poc！')
                        for line in f.readlines():
                            if 'poc_name' in line:
                                try:
                                    # 去除名称信息中不需要的字符
                                    msg = line.split('=')[1].strip().replace('"','').replace("'",'')
                                    break
                                except:
                                    self.__output.output_error('无法正确获取poc name！请检查poc_name处是否正确')
                        # 将poc路径与名称加入到字典当中
                        tmp_line = []
                        tmp_line.append(index)
                        tmp_line.append(tmp_path)
                        tmp_line.append(msg)
                        self.pocs.append(tmp_line)
                        index += 1
        return self.pocs,self.pocs_list

    def read_modules(self):
        '''
            读取存在的poc及其信息
        '''
        # 获取module路径
        try:
            self.__modules_path = os.path.join(self.__now_path,'modules')
        except:
            self.__output.output_error('无法正确获取poc路径，请检查文件是否完整！',False)
        # 获取所有的modules
        index = 0
        for root, dirs, files in os.walk(self.__modules_path):
            if '__pycache__' not in root:
                for i in files:
                    if i != '__init__.py':
                        # 将绝对路径修改为相对路径
                        tmp = 'FrostBlade' + os.sep
                        # 绝对路径
                        tmp_modules_path = root + os.sep + i
                        # 相对路径
                        tmp_path = tmp_modules_path.split(tmp)[2]
                        # 读取文件信息
                        msg = '无module名称信息，请检查module'
                        try:
                            f = open(tmp_modules_path,'r',encoding='UTF-8')
                        except:
                            self.__output.output_error('无法正确打开module，请检查module！')
                        for line in f.readlines():
                            if 'module_name' in line:
                                try:
                                    # 去除名称信息中不需要的字符
                                    msg = line.split('=')[1].strip().replace('"','').replace("'",'')
                                except:
                                    self.__output.output_error('无法正确获取module name！请检查module_name处是否正确')
                        # 将poc路径与名称加入到字典当中
                        tmp_line = []
                        tmp_line.append(index)
                        tmp_line.append(tmp_path)
                        tmp_line.append(msg)
                        self.modules.append(tmp_line)
                        index += 1
        return self.modules

    def search_pocs(self,pwd):
        '''
            从给定的路径中寻找poc文件
        '''
        pocs_list = []
        if os.path.isfile(pwd):
            pocs_list.append(pwd)
        else:
            for root,dirs,files in os.walk(pwd):
                if '__pycache__' not in root and 'exploit' not in root:
                    for i in files:
                        if i != '__init__.py':
                            poc_path = root + os.sep + i
                            pocs_list.append(poc_path)
        return pocs_list

    def read_file(self,pwd):
        '''
        按行读取文件内容
        '''
        msg_list = []
        try:
            for i in open(pwd):
                i=i.strip()
                msg_list.append(i)
            return msg_list
        except:
            self.__output.output_warning('读取文件时出现错误！')
            return msg_list