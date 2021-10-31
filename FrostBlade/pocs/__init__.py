import lib

class Pocs:

    # poc名称
    poc_name = ''
    # 漏洞名称
    vul_name = ''
    # 漏洞编号
    vul_num = ''
    # 漏洞作者
    author = ''
    # 影响的应用
    app_name = ''
    # 影响应用的版本
    app_version = ''
    # 漏洞的具体信息
    msg = ''
    # 使用的payload
    payload = ''
    # poc需要的必须参数
    must_parameter = {
        'target' : ''
    }
    # poc需要的非必需参数
    choo_parameter = {

    }

    def __init__(self) -> None:
        # 扫描的结果信息
        pass

    
    def exploit(self,must_parameter,choo_parameter):
        '''
            进行攻击的函数
        '''
        self.att_msg['target']=must_parameter['target']
        self.parameter = must_parameter

    def get_info(self):
        '''
            获取poc信息的函数
        '''
        msg=[self.poc_name,self.vul_name,self.vul_num,self.author,self.app_name,self.app_version,self.msg]
        return msg
        
