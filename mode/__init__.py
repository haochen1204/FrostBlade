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
    
