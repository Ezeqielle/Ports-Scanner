#!/usr/bin/python3

from socket import *
import optparse
from threading import *
from termcolor import colored

####### All ports #######

def multiConnScan(tgtHost,tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        # try connection to HOST by selected PORT
        sock.connect((tgtHost, tgtPort))
        # print succesfull connection in green
        print(colored(f'[+] {tgtPort}/tcp Open', 'green'))
    except:
        # pass if connection fail for clean the output
        pass
    finally:
        # close the socket connection
        sock.close()

def multiPortsScanner(tgtHost):
    try:
        # get the HOST name
        tgtIP = gethostbyname(tgtHost)
    except:
        # if connection fail print HOST in red
        print(colored(f'[-] Unknow host {tgtHost}', 'red'))

    try:
        # get the HOST IP addr
        tgtName = gethostbyaddr(tgtIP)
        # if connection succes print HOST in yellow
        print(colored(f'[+] Scan result for: {tgtName(0)}', 'yellow'))
    except:
        # if connection succes print HOST in yellow
        print(colored(f'[+] Scan result for: {tgtIP}', 'yellow'))

    # set default timeout connection to HOST
    setdefaulttimeout(1)

    # iter all ports and send each to multiConnScan()
    for tgtPort in range(0,65536):
        t = Thread(target=multiConnScan, args=(tgtHost, int(tgtPort)))
        t.start()    

####### Specific ports #######

def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        # try connection to HOST by selected PORT
        sock.connect((tgtHost, tgtPort))
        # print succesfull connection in green
        print(colored(f'[+] {tgtPort}/tcp Open', 'green'))
    except:
        # print the fail connection in red
        print(colored(f'[-] {tgtPort}/tcp Closed', 'red'))
    finally:
        sock.close()

def portScanner(tgtHost, tgtPorts):
    try:
        # get the HOST name
        tgtIP = gethostbyname(tgtHost)
    except:
        # if connection fail print HOST in red
        print(colored(f'[-] Unknow host {tgtHost}', 'red'))

    try:
        # get the HOST IP addr
        tgtName = gethostbyaddr(tgtIP)
        # if connection succes print HOST in yellow
        print(colored(f'[+] Scan result for: {tgtName(0)}', 'yellow'))
    except:
        # if connection succes print HOST in yellow
        print(colored(f'[+] Scan result for: {tgtIP}', 'yellow'))
    
    # set default timeout connection to HOST
    setdefaulttimeout(1)

    # iter all selected ports to scan and send each to connScan()
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

####### Main #######

def main():
    # define the usage command for help
    usage = 'Usage: python3 %prog [option] arg'
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('-H', dest='tgtHost', type='string', help='specifiy target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specifiy target post seperate by comma')
    parser.add_option('-a', dest='tgtPorts', action='store_true', default=False, help='scann all ports')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = str(options.tgtPort).split(',')
    tgtPorts = options.tgtPorts

    # return command error
    if tgtHost == None and tgtPort == None:
        print(parser.usage)
        exit(0)

    # if option -a used for scan all 65536 ports
    if tgtHost != None and tgtPorts == True:
        multiPortsScanner(tgtHost)
    
    # else scan specifics ports in -p <port>,<port>
    else:
        portScanner(tgtHost, tgtPort)

# main function
if __name__ == '__main__':
    main()