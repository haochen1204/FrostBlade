import yaml
import os
from lib import output
import lib

output=output.cmd_output()
GraphicalTools = {}
python = ''
PyTools = {}
CustomCommand = {}
Pack = {}
TabCommad = []
fofa_username = ''
fofa_key = ''
def read_config():
    '''
        读取配置文件的函数
    '''
    global GraphicalTools
    global PyTools
    global python
    global CustomCommand
    global Pack
    global TabCommad
    global fofa_username
    global fofa_key
    
    if lib.SYSTYPE == 'windows':
        config_path = os.path.abspath(__file__).replace('lib\\config.py','') + 'FrostBlade_config.yaml'
        work_path = os.path.abspath(__file__).replace('lib\\config.py','')
    else:
        config_path = os.path.abspath(__file__).replace('lib/config.py','') + 'FrostBlade_config.yaml'
        work_path = os.path.abspath(__file__).replace('lib/config.py','')
    os.chdir(work_path)
    try:
        file = open(config_path,encoding='utf-8')
        data = yaml.safe_load(file)
        python = data['python']
        GraphicalTools = data['GraphicalTools']
        PyTools = data['PyTools']
        CustomCommand = data['CustomCommand']
        Pack = data['Pack']
        TabCommad = data['tab']
        fofa_username = data['fofa']['username']
        fofa_key = data['fofa']['key']
    except:
        output.output_error('读取配置文件失败！请检查FrostBlade_config.yaml是否存在！')
    