

class modules:
    # 模块名称
    modules_name = ''
    # 模块作者
    modules_author = ''
    # 模块说明
    modules_explain = ''
    # 必要参数
    must_parameter = {}
    # 选择参数
    choo_parameter = {}
    # 输出结果
    msg = {
        'status' : [],
        'target' : [],
        'msg' : []
    }

    def __init__(self) -> None:
        pass

    def set_parameter(self,must_parameter,choo_paramter):
        '''
            模块设置参数所用函数
        '''
        self.must_parameter = must_parameter
        self.choo_parameter = choo_paramter

    def run(self):
        '''
            模块运行的启动函数
        '''

    def cout(self):
        '''
            结果的输出函数
        '''
        for status,target,msg in zip(self.msg['status'],self.msg['target'],self.msg['msg']):
            if status == 'success':
                print('\033[32m[+] {0:5}    {1:<20}      {2:<20}\033[0m'.format(status,target,msg))
            else:
                print('[-] {0:5}    {1:<20}      {2:<20}'.format(status,target,msg)) 

    
