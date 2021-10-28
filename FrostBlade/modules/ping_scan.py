import threading
import subprocess
import modules

class MOD(modules.module):

    def __init__(self) -> None:
        super().__init__()
        self.module_name= 'ping扫描'
        self.module_author = 'haochen'
        self.module_explain = '通过ping来判断主机是否存活，可以对多个网段的特定ip进行扫描'
        self.must_parameter={
            'ip' : '', 
            'thread' : '100'
        }

    def run(self):
        '''     
            运行函数      
        '''
        thread_num = int(self.must_parameter['thread'])
        i = 0
        ip = self.must_parameter['ip']
        while True:
            if i <= 255 and threading.active_count()-1 < thread_num:
                tmp_ip =  ip.replace('*',str(i))
                thread = threading.Thread(target=self.ping_ip,args=(tmp_ip,))
                thread.start()
                i += 1
            if i > 255 and threading.active_count() == 1:
                self.cout()
                break 
    
    def ping_ip(self,ip): 
        '''
            系统执行的主要函数
        '''                                        
        # 执行系统ping命令，并将执行结果存放在output中
        try:
            output = subprocess.getoutput('ping -c 1 '+ip)
        except Exception as e:
            pass
        # 从output中循环读取数据
        #print('****' + str(output))
        # 判断每行中是否存在TTL，存在则说明ping通，主机存活
        #print(output)
        if output.find('TTL')>=0 or output.find('ttl')>=0:
            #print("[+] {0:^10} is alive".format(ip))
            tmp_msg = []
            tmp_msg.append('success')
            tmp_msg.append(ip)
            tmp_msg.append('is alive')
            self.msg.append(tmp_msg)