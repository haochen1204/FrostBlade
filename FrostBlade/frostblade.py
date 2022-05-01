from lib import console
from lib import message
from lib import config
import sys
import getopt

def main():
    '''
        主函数
    '''
    # 显示工具信息展示头
    message.head()
    config.read_config()
    # 读取命令行选项,若没有则直接进入控制台
    if not len(sys.argv[1:]):
        cmd = console.Console()
        cmd.start()
    else:
        # 读取用户输入的参数
        try:
            opts, args = getopt.getopt(sys.argv[1:], 
            "h",
            ["help",])
        except getopt.GetoptError as err:
            print(str(err))
            message.help()
        # 从opts中读取数据，o为参数,a为参数后带的值
        for o,a in opts:
            if o in ("-h","--help"):    # 如果参数为help，展示help界面
                message.help()
    

if __name__ == '__main__':
    main()
    