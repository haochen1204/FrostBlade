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
    print("使用帮助：")
    print("python3 FrostBlade.py             进入控制台")
    print("python3 FrostBlade.py -h          打开帮助文档")