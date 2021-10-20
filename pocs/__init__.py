import re
import requests
# 数据包中的内容
Pack = {
    'Host': 'www.baidu.com',
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://i.g-fox.cn/',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0'
}

class Pocs:

    # 扫描的结果信息
    att_msg={
        'status' : '',
        'target' : '',
        'payload' : ''
    }
    # poc名称
    poc_name = ''
    # 漏洞名称
    vul_name = ''
    # 漏洞编号
    vul_num = ''
    # 漏洞作者
    author = ''
    # 影响的应用
    app_name = ''
    # 影响应用的版本
    app_version = ''
    # 漏洞的具体信息
    msg = ''
    # poc需要设置的参数
    parameter = {
        'target' : ''
    }

    def __init__(self) -> None:
        pass

    def sacnner(self,parameter):
        '''
            进行扫描的函数
        '''
        self.att_msg['target']=parameter['target']
        self.parameter=parameter
    
    def exploit(self,parameter):
        '''
            进行攻击的函数
        '''
        self.att_msg['target']=parameter['target']
        self.parameter = parameter

    def cout(self):
        '''
            输出结果所用的函数
        '''
        if self.att_msg['status'] == 'success':
            print('\033[32m[+] {0:<10}  {1:<50} {2:<20}\033[0m'.format(self.att_msg['status'],self.att_msg['target'],self.poc_name))
        elif self.att_msg['status'] == 'failed':
            print('[-] {0:<10}  {1:<50} {2:<20}'.format(self.att_msg['status'],self.att_msg['target'],self.poc_name))
        else:
            print('[*] {0:<10}  {1:<50} {2:<20}'.format(self.att_msg['status'],self.att_msg['target'],self.poc_name))


    def show_options(self):
        '''
            输出漏洞信息所用的函数
        '''
        print('     {0:^10}     {1:5}      {2:<100}'.format('pocname','',self.poc_name))
        print('     {0:^10}     {1:5}      {2:<100}'.format('vulname','',self.vul_name))
        print('     {0:^10}     {1:5}      {2:<100}'.format('vulnum','',self.vul_num))
        print('     {0:^10}     {1:5}      {2:<100}'.format('appname','',self.app_name))
        print('     {0:^10}     {1:5}      {2:<100}'.format('appversion','',self.app_version))
        print('     {0:^10}     {1:5}      {2:<100}'.format('author','',self.author))
        if self.att_msg['payload']!='':
            print('     {0:^10}     {1:5}      {2:<100}'.format('payload','',self.att_msg['payload']))
        print('     {0:^10}     {1:5}      {2:<100}'.format('','',self.msg))
