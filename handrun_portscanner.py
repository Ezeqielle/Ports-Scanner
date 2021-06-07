#!/usr/bin/python3

from socket import *
import optparse
from threading import *
from termcolor import colored

####### All ports #######

def multiConnScan(tgtHost,tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print(colored(f'[+] {tgtPort}/tcp Open', 'green'))
    except:
        pass
    finally:
        sock.close()

def multiPortsScanner(tgtHost):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(colored(f'[-] Unknow host {tgtHost}', 'red'))

    try:
        tgtName = gethostbyaddr(tgtIP)
        print(colored(f'[+] Scan result for: {tgtName(0)}', 'yellow'))
    except:
        print(colored(f'[+] Scan result for: {tgtIP}', 'yellow'))

    setdefaulttimeout(1)

    for tgtPort in range(0,65536):
        t = Thread(target=multiConnScan, args=(tgtHost, int(tgtPort)))
        t.start()    

####### Specific ports #######

def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print(colored(f'[+] {tgtPort}/tcp Open', 'green'))
    except:
        print(colored(f'[-] {tgtPort}/tcp Closed', 'red'))
    finally:
        sock.close()

def portScanner(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(colored(f'[-] Unknow host {tgtHost}', 'red'))

    try:
        tgtName = gethostbyaddr(tgtIP)
        print(colored(f'[+] Scan result for: {tgtName(0)}', 'yellow'))
    except:
        print(colored(f'[+] Scan result for: {tgtIP}', 'yellow'))
    
    setdefaulttimeout(1)
    
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

####### Main #######

def main():
    usage = 'Usage: python3 %prog [option] arg'
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('-H', dest='tgtHost', type='string', help='specifiy target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specifiy target post seperate by comma')
    parser.add_option('-a', dest='tgtPorts', action='store_true', default=True, help='scann all ports')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = str(options.tgtPort).split(',')
    tgtPorts = options.tgtPorts

    if tgtHost == None and tgtPort == None:
        print(parser.usage)
        exit(0)

    if tgtHost != None and tgtPorts == True:
        multiPortsScanner(tgtHost)
    
    else:
        portScanner(tgtHost, tgtPort)


if __name__ == '__main__':
    main()