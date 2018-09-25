resultLength = 35


class Colors(object):
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


def title(text):
    length = len(text)
    print('')
    print(Colors.BGYELLOW + Colors.BLACK + repeat(' ', length + 10) + Colors.ENDC)
    print(Colors.BGYELLOW + Colors.BLACK + repeat(' ', 5) + text + repeat(' ', 5) + Colors.ENDC)
    print(Colors.BGYELLOW + Colors.BLACK + repeat(' ', length + 10) + Colors.ENDC)


def subtitle(text):
    print('')
    print(Colors.YELLOW + Colors.BOLD + text + Colors.ENDC)
    print(Colors.YELLOW + '--------------------------------------------' + Colors.ENDC)


def text(name, value):
    if value is None:
        value = '-'
    length = resultLength-len(name)
    print(Colors.GRAY + name + repeat(' ', length) + value + Colors.ENDC)


def success(name, value):
    if value is None:
        value = '-'
    length = resultLength-len(name)
    print(Colors.GREEN + name + repeat(' ', length) + value + Colors.ENDC)


def warning(name, value):
    if value is None:
        value = '-'
    length = resultLength-len(name)
    print(Colors.YELLOW + name + repeat(' ', length) + value + Colors.ENDC)


def error(name, value):
    if value is None:
        value = '-'
    length = resultLength-len(name)
    print(Colors.RED + name + repeat(' ', length) + value + Colors.ENDC)


def repeat(string, length):
    return (string * ((length/len(string))+1))[:length]


def separator():
    print(Colors.GRAY + '--------------------------------------------' + Colors.ENDC)
