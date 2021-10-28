import sys
import os
from lib import file

# 版本信息
version = '0.2'

# 当前使用的路径
Pwd = ''

# 判断是否是windows
IS_WIN = IS_WIN = True if (sys.platform in ["win32", "cygwin"] or os.name == "nt") else False

# 正则表达式
# ip地址
IP_ADDRESS_REGEX = r"\b(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\b"
# ip地址和端口
IP_ADDRESS_WITH_PORT_REGEX = r"\b(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]):[\d]{2,5}\b"
# url地址
URL_ADDRESS_REGEX = r"(?:(?:https?):\/\/|www\.|ftp\.)(?:\([-a-zA-Z0-9+&@#\/%=~_|$?!:,.]*\)|[-a-zA-Z0-9+&@#\/%=~_|$?!:,.])*(?:\([-a-zA-Z0-9+&@#\/%=~_|$?!:,.]*\)|[a-zA-Z0-9+&@#\/%=~_|$])"
# url地址范围
URL_DOMAIN_REGEX = r"(?:www)?(?:[\w-]{2,255}(?:\.\w{2,6}){1,3})(?:/[\w&%?#-]{1,300})?(?:\:\d+)?"
# 内网ip地址
LOCAL_IP_ADDRESS_REGEX = r"(^10\.)|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)|(^192\.168\.)"

# 输出信息的头部
FIELD_NAMES = {
    'pocs' : ['INDEX','POC PATH','POC NAME'],
    'modules' : ['INDEX', 'MODULE PATH', 'MODULE NAME'],
    'search' : ['INDEX', 'PATH'],
    'module' : ['NAME', 'AUTHOR', 'EXPLAIN'],
    'parameter' : ['PARAMETER','','VALUE'],
    'module result' : ['STATUS','TARGET','MSG'],
    'poc' : ['POC NAME','VUL NAME','VUL NUM','AUTHOR','APP NAME','APP VERSION','EXPLAIN'],
    'poc result' : ['STATUS','TARGEt','POC NAME','MSG']
}


# poc的路径和poc的目录信息
POCS,POCS_LIST = file.file().read_pocs()
# 模块的信息
MODULES = file.file().read_modules()

# poc的返回结果
POC_MESSAGE = []