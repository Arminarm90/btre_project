#!/usr/bin/env python
# src:https://gist.github.com/jtriley/1108174
import os
import shlex
import struct
import platform
import subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_terminal_size():
    """ getTerminalSize()
     - get width and height of console
     - works on linux,os x,windows,cygwin(windows)
     originally retrieved from:
     http://stackoverflow.com/questions/566746/how-to-get-console-window-width-in-python
    """
    current_os = platform.system()
    tuple_xy = None
    if current_os == 'Windows':
        tuple_xy = _get_terminal_size_windows()
        if tuple_xy is None:
            tuple_xy = _get_terminal_size_tput()
            # needed for window's python in cygwin's xterm!
    if current_os in ['Linux', 'Darwin'] or current_os.startswith('CYGWIN'):
        tuple_xy = _get_terminal_size_linux()
    if tuple_xy is None:
        print "default"
        tuple_xy = (80, 25)      # default value
    return tuple_xy
 
 
def _get_terminal_size_windows():
    try:
        from ctypes import windll, create_string_buffer
        # stdin handle is -10
        # stdout handle is -11
        # stderr handle is -12
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        if res:
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom,
             maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
            return sizex, sizey
    except:
        pass
 
 
def _get_terminal_size_tput():
    # get terminal width
    # src: http://stackoverflow.com/questions/263890/how-do-i-find-the-width-height-of-a-terminal-window
    try:
        cols = int(subprocess.check_call(shlex.split('tput cols')))
        rows = int(subprocess.check_call(shlex.split('tput lines')))
        return (cols, rows)
    except:
        pass
 
 
def _get_terminal_size_linux():
    def ioctl_GWINSZ(fd):
        try:
            import fcntl
            import termios
            cr = struct.unpack('hh',
                               fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
            return cr
        except:
            pass
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        try:
            cr = (os.environ['LINES'], os.environ['COLUMNS'])
        except:
            return None
    return int(cr[1]), int(cr[0])

def aligncenter(content,width,height):
    length = len(content)
    if length < width:
        borderlength =int((width - length)/2)
        # print "\n"+"="*(borderlength-1) +" "+ content +" "+ "="*(borderlength-1)+"\n"
        print "\n"
        print (width*"=")
        print " "*(borderlength-1) +" "+Fore.RED +Style.BRIGHT+ content +Style.RESET_ALL+" "+ " "*(borderlength-1)
        print (width*"=")
        print "\n"

from colorama import Fore, Back, Style, init
import time,sys
init()

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.BRIGHT + 'and in dim text')
print(Fore.RESET + Back.RESET + Style.RESET_ALL)
print('back to normal now')

if __name__ == "__main__":
    sizex, sizey = get_terminal_size()
    # print  'width =', sizex, 'height =', sizey
    data = "Simplify"
    aligncenter(content=data, width=sizex, height=sizey)
    time.sleep(2)
    i =0
    for i in range(0,50):
        print "\r"+Back.RED+" "*50+Back.RESET,
        print "\r"+Back.GREEN+" "*(i-2)+str(i)+"%"+Back.RESET ,
        # if i%4 == 0:
        #   print"\\\\",
        # if i%4 == 1:
        #   print"||",
        # if i%4 == 2:
        #   print"//",
        # if i%4 == 3:
        #   print"==",
        # print " "*(50-i),"["+str(i)+"%|50%]",

        time.sleep(0.1)
        sys.stdout.flush()


