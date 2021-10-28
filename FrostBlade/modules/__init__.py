from lib import output

class module:
    # 模块名称
    module_name = ''
    # 模块作者
    module_author = ''
    # 模块说明
    module_explain = ''
    # 必要参数
    must_parameter = {}
    # 选择参数
    choo_parameter = {}
    # 输出结果
    msg = []

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

    def get_info(self):
        '''
            获取模块信息的函数
        '''
        msg = [[self.module_name,self.module_author,self.module_explain]]
        return msg

    def cout(self):
        self.output = output.cmd_output()
        self.output.output_attack(self.msg,'module result')
 
    
