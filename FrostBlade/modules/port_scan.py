import threading
import subprocess
from lib import output
import modules
from socket import *
from ipaddress import ip_address


class MOD(modules.module):

    def __init__(self) -> None:
        super().__init__()
        self.module_name= '端口扫描'
        self.module_author = 'haochen'
        self.module_explain = '''输入要扫描的ip和端口
ip：192.168.1.1-192.168.1.255或192.168.1.1，192.168.1.2...
端口：1-65535或20，21，22....或使用内置端口列表
扫描方式：TCP TCP全连接扫描 SYN TCP半开放扫描 UDP UDP扫描
内置端口列表：all->全端口 simple->简单端口 often(默认)->常用端口
显示：all 显示全部 success 显示攻击成功'''
        self.must_parameter={
            'ip' : ''
        }
        self.choo_parameter={
            'port':'often',
            'pattern':'TCP',
            'thread' : '100',
            'show' : 'success'
        }
        self.output = output.cmd_output()

    def run(self):
        '''     
            运行函数      
        '''
        thread_num = int(self.choo_parameter['thread'])
        i = 0
        ip,port = self.__handler()
        ip_num = 0
        port_num = 0
        setdefaulttimeout(1)
        try:
            command =  getattr(self, "{}_scan".format(self.choo_parameter['pattern']))
            while True:
                if threading.active_count()-1 < thread_num:
                    thread = threading.Thread(target=command,args=(ip[ip_num],port[port_num]))
                    thread.start()
                    port_num+=1
                    if port_num == len(port):
                        ip_num +=1
                        port_num = 0
                    if ip_num == len(ip):
                        break
            while True:
                if threading.active_count() == 1:
                    self.cout()
                    break
        except:
            self.output.output_error('pattern 参数输入错误，未找到该扫描方式')
        
    
    def __handler(self):
        '''
            处理用户输入的ip和端口的函数
        '''
        ip = self.must_parameter['ip']
        port = self.choo_parameter['port']
        ip_list = []
        port_list = []
        # 处理用户输入的ip
        if '-' in ip:
            ip = ip.split('-')
            start = ip_address(ip[0])
            end = ip_address(ip[1])
            while start <= end:
                ip_list.append(str(start))
                start += 1
        elif ',' in ip:
            ip = ip.split(',')
            for i in ip:
                ip_list.append(i)
        else:
            ip_list.append(ip)
        # 处理用户输入的端口
        if '-' in port:
            port = port.split('-')
            start = int(port[0])
            end = int(port[1])
            while start <= end:
                port_list.append(start)
                start+=1
        elif ',' in port:
            port = port.split(',')
            for i in port:
                port_list.append(i)
        elif port == 'all':
            for i in range(0,65536):
                port_list.append(i)
        elif port == 'simple':
            port_list = [21,22,80,137,161,443,445,1900,3306,3389,5353,8080]
        else:
            port_list = [21,22,23,25,53,53,80,81,110,111,123,123,135,137,139,161,389,443,445,465,500,515,520,523,548,623,636,873,902,1080,1099,1433,1521,1604,1645,1701,1883,1900,2049,2181,2375,2379,2425,3128,3306,3389,4730,5060,5222,5351,5353,5432,5555,5601,5672,5683,5900,5938,5984,6000,6379,7001,7077,8080,8081,8443,8545,8686,9000,9001,9042,9092,9100,9200,9418,9999,11211,27017,37777,50000,50070,61616]
        return ip_list,port_list

    def TCP_scan(self,ip,port):
        '''
            TCP扫描
        '''
        tmp_msg = []
        try:
            s = socket(AF_INET,SOCK_STREAM)
            s.connect((ip,port))
            tmp_msg.append('success')
            tmp_msg.append(ip+':'+str(port))
            tmp_msg.append('is open!')
            self.msg.append(tmp_msg)
            s.close()
        except:
            if self.choo_parameter['show'] == 'all':
                tmp_msg.append('failed')
                tmp_msg.append(ip+':'+str(port))
                tmp_msg.append('is close!')
                self.msg.append(tmp_msg)
    
        