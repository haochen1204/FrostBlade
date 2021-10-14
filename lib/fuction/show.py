from lib import config

def show_tools():
    '''
        用于展示工具中集成的其他工具
    '''
    print("\nYou can use these in FrostBlade:")
    for i in config.ToolCommand:
        print(i)
    for i in config.GraphicalTools:
        print(i)
    for i in config.PyTools:
        print(i)
    print('')

def show_pocs():
    print('')
    for i in config.PocPwd:
        for j in config.PocFile[i]:
            print(i+'/'+j)