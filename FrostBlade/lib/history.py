from lib import config
import readline
import rlcompleter
import atexit
import os
import yaml

class MyCompleter(object):  # Custom completer

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options
                                    if s and s.startswith(text)]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        # return match indexed by state
        try:

            return self.matches[state]
        except IndexError:
            return None

def read_config_tab():
    '''
      读取配置文件中需要补全的命令
    '''
    TabCommand = []
    config_path = os.path.abspath(__file__).replace('lib/history.py','') + 'FrostBlade_config.yaml'
    try:
      file = open(config_path,encoding='utf-8')
      data = yaml.safe_load(file)
      TabCommand = data['tab']
      TabCommand += data['GraphicalTools'].keys()
      TabCommand += data['PyTools'].keys()
      TabCommand += data['CustomCommand'].keys()
    except:
      pass
    return TabCommand

completer = MyCompleter(read_config_tab())
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')
# 显示历史命令
histfile = os.path.join(os.path.abspath(__file__).replace('lib/history.py','tmp'), '.pythonhistory')
try:
    # 判断文件是否存在不存在则创建一个
    if not os.path.isfile(histfile):
        fd = open(histfile, mode="w", encoding="utf-8")
        fd.close()
    readline.read_history_file(histfile)
except IOError:
    pass
atexit.register(readline.write_history_file,histfile)
del os,histfile,readline,rlcompleter