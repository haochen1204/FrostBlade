import importlib
import re
from lib import config


class attack:

    global poc
    global target
    target = ''

    def set_poc():
        '''
            设置要使用的poc
        '''
        global poc
        pwd = config.Pwd
        pwd=pwd.replace('/','.')
        pwd=pwd.replace('.py','')
        poc = importlib.import_module(pwd).POC

    def show_options():
        print('')
        print("     {0:^10}     {1:5}      {2:20}".format('POC','',poc.pocName))
        print("     {0:^10}     {1:5}      {2:20}".format('Target','YES',target))
        return

    def exploit():
        if 'scanner' in poc.pocName:
            judge=poc.scanner(target)
        elif 'exploit' in poc.pocName:
            poc.exploit(target)
        if judge == True:
            print('YEs')
        return

    def set_msg(msg,urll):
        global target
        if msg == 'target':
            target = urll
        return