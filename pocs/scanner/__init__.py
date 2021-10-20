import requests
import pocs

class Pocs:

    # 扫描的结果信息
    att_msg={
        'status' : '',
        'target' : '',
        'payload' : ''
    }
    # poc名称
    poc_name = ''
    # poc路径
    poc_pwd = ''
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
    
    def __init__(self) -> None:
        pass

    def sacnner(self,target):
        '''
            进行扫描的函数
        '''
        self.att_msg['target']=target
    
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
        print('     {0:^10}     {1:5}      {2:<100}'.format('pocpwd','',self.poc_pwd))
        print('     {0:^10}     {1:5}      {2:<100}'.format('vulname','',self.vul_name))
        print('     {0:^10}     {1:5}      {2:<100}'.format('vulnum','',self.vul_num))
        print('     {0:^10}     {1:5}      {2:<100}'.format('appname','',self.app_name))
        print('     {0:^10}     {1:5}      {2:<100}'.format('appversion','',self.app_version))
        print('     {0:^10}     {1:5}      {2:<100}'.format('author','',self.author))
        if self.att_msg['payload']!='':
            print('     {0:^10}     {1:5}      {2:<100}'.format('payload','',self.att_msg['payload']))
        print('     {0:^10}     {1:5}      {2:<100}'.format('','',self.msg))
