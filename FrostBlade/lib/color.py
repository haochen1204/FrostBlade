from colorama import init, Fore, Back, Style

init(autoreset=False)

class Colored(object):
    #  前景色:红色  背景色:默认
    def red(self, s):
        return Fore.LIGHTRED_EX + s + Fore.RESET
    #  前景色:绿色  背景色:默认
    def green(self, s):
        return Fore.LIGHTGREEN_EX + s + Fore.RESET
    def yellow(self, s):
        return Fore.LIGHTYELLOW_EX + s + Fore.RESET
    def white(self,s):
        return Fore.LIGHTWHITE_EX + s + Fore.RESET
    def blue(self,s):
        return Fore.LIGHTBLUE_EX + s + Fore.RESET
    def magenta(self,s):
        return Fore.LIGHTMAGENTA_EX + s + Fore.RESET
    def cyan(self,s):
        return Fore.CYAN + s + Fore.RESET

    def red_list(self,s):
        tmp = []
        for i in s:
            i = self.red(i)
            tmp.append(i)
        return tmp

    def green_list(self,s):
        tmp = []
        for i in s:
            i = self.green(i)
            tmp.append(i)
        return tmp

    def yellow_list(self,s):
        tmp = []
        for i in s:
            i = self.yellow(i)
            tmp.append(i)
        return tmp
