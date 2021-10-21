import importlib

class modmessage:

    def init(self,mod_pwd):
        '''
            初始化并引入模块
        '''
        self.pwd = mod_pwd
        self.pwd=self.pwd.replace('/','.')
        self.pwd=self.pwd.replace('.py','')
        self.mod = importlib.import_module(self.pwd).MOD()
        self.must_parameter = self.mod.must_parameter
        self.choo_parameter = self.mod.choo_parameter
        self.mod_name = self.mod.modules_name
        self.mod_explain = self.mod.modules_explain
        self.mod_author = self.mod.modules_author

    def show_parameter(self):
        '''
            展示模块需要的参数
        '''
        print('')
        print('     {0:^10}     {1:^5}     {2:<10}'.format(self.mod_name,'',self.mod_author))
        print('                 {0:<20}'.format(self.mod_explain))
        print('')
        keys = self.must_parameter.keys()
        for i in keys:
            print('     {0:^10}     {1:^5}     {2:<10}'.format(i,'YES',self.must_parameter[i]))
        keys = self.choo_parameter.keys()
        for i in keys:
            print('     {0:^10}     {1:^5}     {2:<10}'.format(i,'NO',self.choo_parameter[i]))

    def clear_list(self):
        '''
            清空参数
        '''
        self.must_parameter = {}
        self.choo_parameter = {}

    def set_parameter(self,msg,input):
        '''
            设置模块需要的参数
        '''
        keys = self.must_parameter.keys()
        if msg in keys:
            self.must_parameter[msg] = input
            return True
        keys = self.choo_parameter.keys()
        if msg in keys:
            self.choo_parameter[msg] = input
            return True
        return False
    
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
            print('')
            self.mod.run()

    
