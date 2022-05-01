from lib import output
from lib import file
from lib import config
from lib import message
from lib import module
from lib import attack
import lib
import os
import appscript
import threading

class handler():

    def __init__(self):
        '''
            初始化函数
        '''
        self.output = output.cmd_output()
        self.file = file.file()
        self.input_command = ''
        self.input_args = ''
        self.last_command = ''
        self.search_msg = []

    def __parse_line(self, line):
        '''
            将输入的命令与参数分开
        '''
        command, _, arg = line.strip().partition(" ")
        return command, arg.strip()

    def command_new(self,agrs):
        '''
            开启新的窗口
        '''
        if agrs == 'windows':
            try:
                command = config.python + ' ' + lib.NOWORK + '/frostblade.py'
                if lib.SYSTYPE == 'macos':
                    appscript.app('Terminal').do_script(command)
                    self.output.output_info('new terminal is running!')
                elif lib.SYSTYPE == 'windows':
                    os.system('start cmd.exe /c '+command)
                    self.output.output_info('new cmd is running!')
                elif lib.SYSTYPE == 'linux':
                    os.system("gnome-terminal -e '%s"%command)
                    self.output.output_info('new terminal is running!')
                else:
                    self.output.output_error('未查询到您的操作系统类型，无法打开新的终端！')
            except Exception as e:
                self.output.output_error(e)
        else:
            self.output.output_error('Unknown new sub-command '+agrs+'. What do you want to do?',False)

    def command_show(self,agrs):
        '''
            命令处理函数
        '''
        self.input_command, self.input_args = self.__parse_line(agrs)
        if self.input_command in config.CustomCommand.keys() and self.input_args == 'help':
            func = '_show_tools_help'
        else:
            func = '_show_' + self.input_command
        try:
            common_handler = getattr(self,func)
            common_handler(self.input_command,self.input_args)
        except AttributeError:
            self.output.output_error('Unknown show sub-command '+agrs+'. What do you want to show?',False)
        except EOFError:
            self.output.output_error("FrostBlade stopped",False)

    def _show_pocs(self,command,args):
        '''
            展示poc的函数
        '''
        if args != '' or command == '':
            self.output.output_warning("Unknow this agrs '{}'! FrostBlade have been run '{}'!".format(self.input_args,self.input_command),False)
        elif lib.POCS != '':
            self.output.output_message(lib.POCS,command)
        else:
            real_command = 'read_'+command
            try:
                command_handler = getattr(self.file,real_command)
                pocs = command_handler()
            except EOFError:
                self.output.output_error("FrostBlade stopped",False) 
            self.output.output_message(pocs,command)
        self.last_command = command

    def _show_modules(self,command,args):
        '''
            展示模块的函数
        '''
        if args != '' or command == '':
            self.output.output_warning("Unknow this agrs '{}'! FrostBlade have been run '{}'!".format(self.input_args,self.input_command),False)
        elif lib.MODULES != '':
            self.output.output_message(lib.MODULES,command)
        else:
            real_command = 'read_'+command
            try:
                command_handler = getattr(self.file,real_command)
                modules = command_handler()
            except EOFError:
                self.output.output_error("FrostBlade stopped",False)
            self.output.output_message(modules,command) 
        self.last_command = command

    def _show_info(self,command,args):
        '''
            展示基本信息的函数
        '''
        if 'module' in lib.Pwd:
            self.output.output_message(self.mod.info_message,'module')
        elif 'pocs' in lib.Pwd:
            self.output.output_message(self.mod.get_info(),'poc')
        else:
            self.output.output_error('请先选择使用的poc/module!')

    def _show_options(self,command,args):
        '''
            显示需要的参数的函数
        '''
        if lib.Pwd != '':
            self.output.output_message(self.mod.get_parameter(),'parameter')
        else:
            self.output.output_error('请先选择使用的poc/module!')

    def _show_tools(self,command,args):
        '''
            显示集成工具的函数
        '''
        msg = 'you can use these tools in FrostBlade!\n'
        for i in config.GraphicalTools.keys():
            msg += i + '\n'
        for i in config.PyTools.keys():
            msg += i + '\n'
        self.output.output_info(msg)

    def _show_tools_help(self,command,args):
        '''
            显示工具自定义命令的函数
        '''
        tmp_msg = []
        msg = []
        for i in config.CustomCommand[command].keys():
            tmp_msg.append(i)
            tmp_msg.append(config.CustomCommand[command][i])
            msg.append(tmp_msg)
            tmp_msg = []
        self.output.output_info(command+' custom command:')
        self.output.output_message(msg,'tools help')

    def command_use(self,args):
        '''
            选择参数的模块
        '''
        tmp_pwd = ''
        if args.isdigit() == True:
            index = int(args)
            try:
                if self.last_command == 'pocs':
                    tmp_pwd=lib.POCS[index][1]
                    lib.Pwd = tmp_pwd
                elif self.last_command == 'modules':
                    tmp_pwd=lib.MODULES[index][1]
                    lib.Pwd = tmp_pwd
                elif self.last_command == 'search':
                    tmp_pwd=self.search_msg[index][1]
                    lib.Pwd = tmp_pwd
                else:
                    self.output.output_error('不明白您输入的参数，请先使用show pocs 或者 show modules查看存在的poc/module！',False)
            except IndexError:
                tmp_pwd == 'error'
                self.output.output_error('您输入的参数有误，请重新输入！',False)
        else:
            if lib.IS_WIN:
                args = args.replace('/','\\')
            for i in lib.POCS:
                if i[1] == args:
                    tmp_pwd = args 
            for i in lib.MODULES:
                if i[1] == args:
                    tmp_pwd = args
            if args in lib.POCS_LIST:
                tmp_pwd = args
            if tmp_pwd == '':
                self.output.output_error('您输入的poc/module路径有误！请输入正确的poc/module路径！',False)
            else:
                lib.Pwd = tmp_pwd
        if 'modules' in lib.Pwd:
            self.mod = module.modmessage(lib.Pwd)
        elif 'pocs' in lib.Pwd:
            self.mod = attack.attack(lib.Pwd)
        
    def command_back(self,args):
        '''
            退出的某个poc/module的参数
        '''
        if args != '':
            self.output.output_error('参数错误！无法理解您输入的参数：'+args,False)
        else:
            lib.Pwd = ''

    def command_clear(self,args):
        '''
            清空内容的函数
        '''
        if lib.SYSTYPE == 'windows':
            os.system('cls')
        else:
            os.system('clear')

    def command_exit(self,args):
        '''
            退出工具的函数
        '''
        # 手动产生异常，让工具退出
        raise KeyboardInterrupt

    def command_search(self,args):
        '''
            查找poc/module的函数
        '''
        index = 0
        for i in lib.POCS:
            tmp_msg = []
            if args in i[1]:
                tmp_msg.append(index)
                tmp_msg.append(i[1])
                self.search_msg.append(tmp_msg)
                index += 1
        for i in lib.MODULES:
            tmp_msg = []
            if args in i[1]:
                tmp_msg.append(index)
                tmp_msg.append(i[1])
                self.search_msg.append(tmp_msg)
                index += 1
        self.output.output_message(self.search_msg,'search')
        self.last_command = 'search'

    def command_help(self,args):
        '''
            帮助文档
        '''
        self.output.output_info('FrosetBlade help:')
        message.help()
    
    def command_run(self,args):
        '''
            打开或使用某些工具的函数
        '''
        command, _, arg = args.strip().partition(" ")
        if command in config.GraphicalTools.keys():
            os.system(config.GraphicalTools[command]) 
            self.output.output_info(command+' is running!',False)
        elif command in config.PyTools.keys():
            args=args.replace(command,config.PyTools[command])
            for i in config.CustomCommand[command].keys():
                args=args.replace(i,config.CustomCommand[command][i],1)
            self.output.output_info(args + ' is running! ')
            os.system(args)
        else:
            self.output.output_error('请检查您输入的工具名称，或移步至config.py配置！',False)

    def command_runnohup(self,args):
        '''
            在后台运行工具的函数
        '''
        command, _, arg = args.strip().partition(" ")
        file = ''
        args_command = ''
        if command in config.PyTools.keys():
            args_command=args.replace(command,config.PyTools[command])
            for i in config.CustomCommand[command].keys():
                args_command=args_command.replace(i,config.CustomCommand[command][i],1)
            if 'to' in args:
                args_list = args_command.rsplit('to',1)
                args_command = args_list[0]
                if len(args_list) >= 1:
                    file = args_list[1].strip()
            t = threading.Thread(target=self._runnohup,args=(args_command,file))
            t.start()
            self.output.output_info(args_command+' is running!')
        elif command in config.GraphicalTools.keys():
            os.system(config.GraphicalTools[command]) 
            self.output.output_info(command+' is running!',False)
            self.output.output_warning('But ' + command + ' do not need use runnohup to run in the background!')
        else:
            self.output.output_error('请检查您输入的工具名称，或移步至config.py配置！',False)

    def _runnohup(self,command,file=''):
        '''
            后台运行工具时线程调用的工具
        '''
        msg = os.popen(command)
        if file != '':
            f = open(file,'w')
            f.write(msg.read())
            f.close()
        self.output.output_info(command + ' already completed!',True)
        if file != '':
            self.output.output_info('you can see result in ' + file)

    def command_set(self,args):
        '''
            设置参数的函数
        '''
        tmplist = args.split()
        command_list = tmplist[::2]
        arg_list = tmplist[1::2]
        arg=dict(zip(command_list,arg_list))
        for i in command_list:
            if i in self.mod.must_parameter.keys():
                if i in arg.keys():
                    self.mod.must_parameter[i] = arg[i]
                else:
                    self.output.output_error('请输入参数 ' + i + ' 的值！')
            elif i in self.mod.choo_parameter.keys():
                if i in arg.keys():
                    self.mod.choo_parameter[i] = arg[i]
                else:
                    self.output.output_error('请输入参数 ' + i + ' 的值！')
            else:
                self.output.output_error('参数 ' + i + ' 不存在！请输入正确的参数！')
                break

    def command_exploit(self,args):
        '''
            运行开始攻击的函数
        '''
        if self.mod.judge():
            self.mod.run()