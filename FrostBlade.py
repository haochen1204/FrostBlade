from lib import config
from lib import cmd
from lib.fuction import file
import sys
import getopt


def head():
    '''
    显示工具的开头展示信息
    '''
    print("""
         ________                        _   ______   __                __        
        |_   __  |                      / |_|_   _ \ [  |              |  ]       
          | |_ \_|_ .--.   .--.   .--. `| |-' | |_) | | |  ,--.    .--.| | .---.  
          |  _|  [ `/'`\]/ .'`\ \( (`\] | |   |  __'. | | `'_\ : / /'`\\' |/ /__\\\\ 
         _| |_    | |    | \__. | `'.'. | |, _| |__) || | // | |,| \__/  || \__., 
        |_____|  [___]    '.__.' [\__) )\__/|_______/[___]\\'-;__/ '.__.;__]'.__.'
    """)
    print("                 冰霜之刃（霜刃）        version  " + config.version)
    print("                                         个人博客 https://www.haochen1204.com")
    print("                                         github   https://github.com/haochen1204/FrostBlade") 
    print("")
       
def help():
    '''
    显示帮助文档
    '''
    print("使用帮助：")
    print("python3 FrostBlade.py             进入控制台")
    print("python3 FrostBlade.py -h          打开帮助文档")
    return

def main():
    '''
    主函数
    '''
    # 显示工具信息展示头
    head()
    # 读取poc文件信息
    file.read_file('pocs')
    file.read_file('mode')
    # 读取命令行选项,若没有则直接进入控制台
    if not len(sys.argv[1:]):
        cmd.cmd()
    else:
        # 读取用户输入的参数
        try:
            opts, args = getopt.getopt(sys.argv[1:], 
            "h",
            ["help",])
        except getopt.GetoptError as err:
            print(str(err))
            help()
        # 从opts中读取数据，o为参数,a为参数后带的值
        for o,a in opts:
            if o in ("-h","--help"):    # 如果参数为help，展示help界面
                help()
    

if __name__ == '__main__':
    main()
    