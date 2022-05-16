import pocs
from lib import config
import re
import requests
import urllib3
from colorama import init
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=False) 

class POC(pocs.Pocs):

    def __init__(self):
        '''
            初始化函数
        '''
        # 根据漏洞的信息进行定义
        super().__init__()
        self.poc_name='weblgic 任意文件上传漏洞'
        self.vul_name='weblgic 任意文件上传漏洞'
        self.vul_num='CVE-2018—2894'
        self.app_name='weblgic'
        self.app_version='10.3.6 12.1.3 12.2.1'
        self.author='haochen'
        self.msg="在知道部署应用到web目录以及ws_utc/config.do存在的情况下可以利用"
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
        self.payload='/ws_utc/config.do'
        if re.search('/$',url):
            url=url[0:len(url)-1]
        target = url + self.payload
        try:
            response = requests.get(target,headers=head)
            # 攻击完成后需要将攻击的结果写入
            if response.status_code == 200:
                att_msg['status'] = 'success'
                att_msg['msg'] = '存在漏洞,请尝试进行攻击'
            else:
                att_msg['status']='failed'
                att_msg['msg']='不存在漏洞，网站返回值为: '+str(response.status_code) 
        except:
            att_msg['status']='error'
            att_msg['msg']='无法正确访问网站'
        return att_msg