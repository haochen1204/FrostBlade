import yaml
import os
from lib import output

output=output.cmd_output()
GraphicalTools = {}
python = ''
PyTools = {}
CustomCommand = {}
Pack = {}
TabCommad = []

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
    except:
        output.output_error('读取配置文件失败！请检查FrostBlade_config.yaml是否存在！')
    