from lib import output
from lib import handler
from lib import color
import lib
import subprocess
import shlex
import chardet

class Console:
    
    def __init__(self):
        '''
            创建类
        '''
        self.input_args = ''
        self.input_command = ''
        self.output=output.cmd_output()
        self.handler = handler.handler()

    def __parse_line(self, line):
        '''
            将输入的命令与参数分开
        '''
        command, _, arg = line.strip().partition(" ")
        return command, arg.strip()
    
    def __prompt(self):
        '''
            输出提示输入的信息
        '''
        if lib.Pwd == '':
            return 'FrostBlade > '
        else:
            self.color = color.Colored()
            pwd = self.color.blue(lib.Pwd)
            return 'FrostBlade ( '+ pwd +' ) > '

    def __get_command_handler(self, command):
        '''
            处理输入的命令
        '''
        try:
            # 尝试将用户输入的命令作为函数执行
            command_handler = getattr(self.handler, "command_{}".format(command))
        except AttributeError:
            # 将命令与参数作为系统命令去执行
            cmd = self.input_command + ' ' + self.input_args
            # 得到系统命令执行结果的回显并打印
            for line in self.__exec_cmd(cmd):
                result_encoding = chardet.detect(line)['encoding']
                if result_encoding:
                    print(line.decode(result_encoding))
            # 提示用户输入的命令被当作系统命令执行
            self.output.output_warning("FrostBlade Unknown this command, and run it on system: '{}'".format(command),False)
        return command_handler

    def __exec_cmd(self,cmd):
        '''
            系统命令的执行函数
        '''
        cmd = shlex.split(cmd)
        out_data = b''
        try:
            p = subprocess.Popen(
                cmd, shell=False, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
            while p.poll() is None:
                line = p.stdout.read()
                out_data += line
        except Exception as ex:
            self.output.output_error("Execute cmd error {}".format(str(ex)),False)
        encoding = chardet.detect(out_data).get('encoding')
        encoding = encoding if encoding else 'utf-8'
        if lib.IS_WIN:
            out_data = out_data.split(b'\r\n\r\n')
        else:
            out_data = out_data.split(b'\n\n')
        return out_data

    def start(self):
        '''
            系统运行的主要函数
        '''
        while True:
            try:
                # 读取用户输入并分割成命令和参数
                self.input_command, self.input_args = self.__parse_line(input(self.__prompt()))
                # 将命令全部转为小写
                command = self.input_command.lower()
                if not command:
                    continue
                # 尝试获取命令所对应的函数或将命令作为系统命令执行
                command_handler = self.__get_command_handler(command)
                # 执行上一步获取到的函数
                if command_handler != None:
                    command_handler(self.input_args)
            except EOFError:
                self.output.output_error("Pocsuite stopped",True)
                break
            except KeyboardInterrupt:
                self.output.output_info("User Quit",True)
                break
            except UnboundLocalError:
                pass

