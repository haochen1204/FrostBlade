import requests
from lib import config

class POC:
    #PoC信息字段，需要完整填写全部下列信息
    version = '1'#PoC版本，默认为1
    author = ['blh']#此PoC作者
    vulDate = '2014-11-03'#漏洞公开日期
    createDate = '2020-01-13'#编写PoC日期
    updateDate = '2020-01-13'#更新PoC日期，默认与createDate一样
    name = 'CMSEasy 5.5 /celive/live/header.php SQL注入漏洞'#PoC名称
    appName = 'CMSEasy'#漏洞应用名称
    appVersion = '5.5'#漏洞影响版本
    vulType = 'SQL Injection'#漏洞类型
    desc = '''漏洞描述'''#在漏洞描述填写
    install_requires = []#PoC依赖的第三方模块，尽量不要使用第三方模块，必要时参考后面给出的参考链接
    pocDesc = '''PoC用法描述'''#在PoC用法描述填写

    def scanner():
        head = config.Pack
        url = 'http://127.0.0.1:8080/xxx/..;/admin/'
        response = requests.get(url,headers=head)
        if response.status_code == 200:
            print('run')
        return

    def attack():
        return 0