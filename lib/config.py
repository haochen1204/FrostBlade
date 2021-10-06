# 版本信息
version = "v0.0000001"
# 系统命令
SystemCommand = ['ping','ifconfig','ipconfig']
# 工具命令(配置好环境变量，可以直接在系统中使用的工具)
ToolCommand = ['nmap','sqlmap','msfvenom']
# 图形化工具打开指令
GraphicalTools = {
                    'behinder' : 'nohup java -jar /Users/haochen/tool/Behinder/Behinder.jar > system.out &',
                    'brup' : 'nohup java -Xbootclasspath/p:/Users/haochen/tool/burp/burp-loader-keygen-jas502n.jar -jar /Users/haochen/tool/burp/burpsuite_pro_v2.0.11beta.jar > system.out &',
                    'cs' : 'cd /Users/haochen/tool/CobaltStrike4.3/ && ./csgo.sh',
                    'shiro_attack' : 'nohup java -jar /Users/haochen/tool/loophole/shiro/shiro_attack-2.0.jar > system.out &'
                }
# python工具(指需要python3 或 python2来进行启动的工具或其他需要在命令行中手动启动的工具)
PyTools = {
            'xray' : '/Users/haochen/tool/xray/xray',
            'dirsearch' : 'python3 /Users/haochen/tool/dirsearch/dirsearch.py'
        }
