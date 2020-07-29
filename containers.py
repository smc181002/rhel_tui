import os

def containerOption():
    return int(input(''' choose from these options (Container Operations):
    [1] check running containers
    [2] create container
    [3] start container
    [4] stop container
    [4] create a volume
    [5] create a network
    [6] save a container
    [0] back\n'''))
    
def container(opt):
    if opt == 1:
        os.system('docker ps')
    elif opt == 2:
        image_name = input('Enter your image name: ')
        cont_name = input('Enter your container name here: ')
        if cont_name:
            os.system('docker create --name {0} {1}'.format(cont_name, image_name))
        else:
            os.system('docker create {}'.format(image_name))
    elif opt == 0:
        return 0
    else:
        print('you have choosen {0}'.format(opt)) 
    return 1


