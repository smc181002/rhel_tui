import os
from containers import *

from time import sleep
# import sys
def title():    
    os.system('clear')
    os.system('tput setaf 4') # color blue
    print('Welcome to flash inteface'.center(os.get_terminal_size().columns))
    os.system('tput sgr0') # reset color

def exitProtocol():
    print('Exiting. . .')
    sleep(0.4)
    os.system('clear')
    exit()

def menuOne():
    return int(input(''' choose from these options:
    [1] Container Operations
    [2] Newtorking Opetations
    [3] User Modifications
    [4] Web-Server Options
    [5] Miscellaneous
    [0] exit\n'''))
    

while True:
    title()
    oneAns = menuOne() 
    if (oneAns == 0): # zero is the exit protocol
        exitProtocol()
    elif (oneAns == 1):
        os.system('clear')
        while True:
            try:
                if container(containerOption()):
                    pass
                else:
                    break
                input('press any key to continue..')
                os.system('clear')    
            except ValueError: 
                os.system('clear') 
                continue
    else:
        print('you have choosen: {0}'.format(oneAns))
        print('test')
        input()
        os.system('clear')
