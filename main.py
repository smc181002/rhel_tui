import os
from time import sleep
# import sys

def menuOne():
    oneAns = int(input(''' choose from these options:
    [1] Container Operations
    [2] Newtorking Opetations
    [3] User Modifications
    [4] Web-Server Options
    [5] Miscellaneous
    [0] exit\n'''))
    return oneAns

os.system('clear')
print('Welcome to flash inteface'.center(os.get_terminal_size().columns))

oneAns = menuOne()
if (oneAns == 0):
    print('Exiting. . .')
    sleep(0.4)
    os.system('clear')

    exit()
else:
    print('you have choosen: {0}'.format(oneAns))

input()
os.system('clear')
