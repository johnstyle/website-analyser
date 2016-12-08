resultLength = 35

class colors:
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MANGENTA = '\033[35m'
    CYAN = '\033[36m'
    GRAY = '\033[37m'
    BGRED = '\033[41m'
    BGGREEN = '\033[42m'
    BGYELLOW = '\033[43m'
    BGBLUE = '\033[44m'
    BGMANGENTA = '\033[45m'
    BGCYAN = '\033[46m'
    BGGRAY = '\033[47m'



def title( text ):
    length = len(text)
    print('')
    print(colors.BGYELLOW + colors.BLACK + repeat(' ', length + 10) + colors.ENDC)
    print(colors.BGYELLOW + colors.BLACK + repeat(' ', 5) + text + repeat(' ', 5) + colors.ENDC)
    print(colors.BGYELLOW + colors.BLACK + repeat(' ', length + 10) + colors.ENDC)

def subtitle( text ):
    print('')
    print(colors.YELLOW + colors.BOLD + text + colors.ENDC)
    print(colors.YELLOW + '--------------------------------------------' + colors.ENDC)

def text( name, value ):
    if value is None:
        value = '-'
    length = resultLength-len(name)
    print(colors.GRAY + name + repeat(' ', length) + value + colors.ENDC)

def success( name, value ):
    if value is None:
        value = '-'
    length = resultLength-len(name)
    print(colors.GREEN + name + repeat(' ', length) + value + colors.ENDC)

def warning( name, value ):
    if value is None:
        value = '-'
    length = resultLength-len(name)
    print(colors.YELLOW + name + repeat(' ', length) + value + colors.ENDC)

def error( name, value ):
    if value is None:
        value = '-'
    length = resultLength-len(name)
    print(colors.RED + name + repeat(' ', length) + value + colors.ENDC)

def repeat(string, length):
   return (string * ((length/len(string))+1))[:length]
