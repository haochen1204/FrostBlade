# 图形化工具打开指令
GraphicalTools = {
                    'behinder' : 'nohup java -jar ./tools/Behinder/Behinder.jar > ../system.out &',
                    'brup' : 'nohup java -Xbootclasspath/p:./tools/burp/burp-loader-keygen-jas502n.jar -jar ./tools/burp/burpsuite_pro_v2.0.11beta.jar > ../system.out &',
                    'cs' : 'cd ./tools/CobaltStrike4.3/ && ./csgo.sh',
                    'shiro_attack' : 'nohup java -jar ./tools/shiro/shiro_attack-2.0.jar > ../system.out &'
                }
# python工具(指需要python3 或 python2来进行启动的工具或其他需要在命令行中手动启动的工具)
PyTools = {
            'xray' : './tools/xray/xray',
            'dirsearch' : 'python3 ./tools/dirsearch/dirsearch.py'
        }

# 数据包中的内容
Pack = {
    'Host': 'www.baidu.com',
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://i.g-fox.cn/',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0'
}