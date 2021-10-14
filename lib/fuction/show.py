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
    '''
        用于展示工具中所带的poc等
    '''
    print('')
    if config.Pwd == '':
        for i in config.PocPwd:
            for j in config.PocFile[i]:
                if '__init__.py' not in j:
                    print(i+'/'+j)
        print('')
    else:
        for i in config.PocFile[config.Pwd]:
            if '__init__.py' not in i:
                print(i)
            print('')