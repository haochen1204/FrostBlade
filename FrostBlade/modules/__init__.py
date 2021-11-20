from lib import output

class module:
    # 模块名称
    module_name = ''
    # 模块作者
    module_author = ''
    # 模块说明
    module_explain = ''
    # 必要参数
    must_parameter = {}
    # 选择参数
    choo_parameter = {}
    # 输出结果
    msg = []

    def __init__(self) -> None:
        pass

    def set_parameter(self,must_parameter,choo_paramter):
        '''
            模块设置参数所用函数
        '''
        self.must_parameter = must_parameter
        self.choo_parameter = choo_paramter

    def run(self):
        '''
            模块运行的启动函数
        '''

    def get_info(self):
        '''
            获取模块信息的函数
        '''
        msg = [[self.module_name,self.module_author,self.module_explain]]
        return msg

    def cout(self):
        self.output = output.cmd_output()
        self.output.output_attack(self.msg,'module result')
        self.msg = []
 
"""
# 如何编写模块
# 倒入你需要的包，modules必须导入
import threading
import subprocess
import modules

# 创建类，且类名必须为MO，必须继承module类
class MOD(modules.module):

    def __init__(self) -> None:
        # 根据模块等名称进行定义
        super().__init__()
        self.module_name= 'ping扫描'
        self.module_author = 'haochen'
        self.module_explain = '通过ping来判断主机是否存活，可以对多个网段的特定ip进行扫描'
        # 定义需要的参数
        self.must_parameter={
            'ip' : '', 
            'thread' : '100'
        }

    # 自由发挥，但是启动的函数必须为run
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


"""
    
