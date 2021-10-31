import importlib
import  os
from lib import output

class modmessage:

    def __init__(self,mod_pwd):
        '''
            初始化并引入模块
        '''
        self.pwd = mod_pwd
        self.pwd=self.pwd.replace(os.sep,'.')
        self.pwd=self.pwd.replace('.py','')
        self.mod = importlib.import_module(self.pwd).MOD()
        self.must_parameter = self.mod.must_parameter
        self.choo_parameter = self.mod.choo_parameter
        self.info_message = self.mod.get_info()
        self.parameter_message = self.get_parameter()
        self.output = output.cmd_output()

    def judge(self):
        '''
            判断模块所需参数是否设置完成
        '''
        keys = self.must_parameter.keys()
        for i in keys:
            if self.must_parameter[i] == '':
                return False
        return True

    def run(self):
        self.mod.set_parameter(self.must_parameter,self.choo_parameter)
        if self.judge() == True:
            self.output.output_info('module running！')
            self.mod.run()

    
    def get_parameter(self):
        '''
            获取模块需要参数的函数
        '''
        msg = []
        for i in self.must_parameter.keys():
            tmp_list = []
            tmp_list.append(i)
            tmp_list.append('YES')
            tmp_list.append(self.must_parameter[i])
            msg.append(tmp_list)
        for i in self.choo_parameter.keys():
            tmp_list = []
            tmp_list.append(i)
            tmp_list.append('NO')
            tmp_list.append(self.choo_parameter[i])
            msg.append(tmp_list)
        return msg
