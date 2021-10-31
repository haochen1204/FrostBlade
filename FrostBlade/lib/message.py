import lib

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
    print("                 冰霜之刃（霜刃）        version  " + lib.version)
    print("                                         个人博客 https://www.haochen1204.com")
    print("                                         github   https://github.com/haochen1204/FrostBlade") 
    print('')

def help():
    '''
    显示帮助文档
    '''
    print()
    print("使用帮助：")
    print("python3 FrostBlade.py             进入控制台")
    print("python3 FrostBlade.py -h          打开帮助文档")
    print()
    print('命令：')
    print('run')
    print('            [tool name]  运行集成的工具')
    print('help                     查看帮助文档')
    print('show')
    print('            pocs         查看存在的poc')
    print('            modules      查看存在的模块')
    print('            info         查看使用的module/poc的信息')
    print('            options      查看需要设置的参数')
    print('use         ')
    print('            [num]        根据poc/module编号设置使用的poc/module')
    print('            [path]       根据路径设置使用的poc/module')
    print('             	        可以设置为单个poc/module的路径或者poc/scanner下的任意一文件')
    print('                         设置为poc/scanner下任意一文件时代表使用文件中的所有poc进行扫描')
    print('set')
    print('            [parameter1] [args1] [parameter2] [args2]    设置参数')
    print('exploit                   运行')
    print('exit                      退出工具')
    print()
