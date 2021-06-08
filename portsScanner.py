#!/usr/bin/python3

from socket import *
import argparse
from threading import *
from termcolor import colored

####### All ports #######

# take in param the host and ports
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

# take in param the host
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
    exit()  

####### Range port #######

# take in param the host and ports
def rangeConnScan(tgtHost,tgtPort):
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
        # close the socket connection
        sock.close()

# take in param the host and ports
def rangePortsScanner(tgtHost, tgtRPorts):
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

    # iter all ports and send each to rangeConnScan()
    sta = tgtRPorts[0]
    ed = tgtRPorts[1]
    for tgtPort in range(int(sta),int(ed)):
        t = Thread(target=rangeConnScan, args=(tgtHost, int(tgtPort)))
        t.start()
    exit()

####### Specific ports #######

# take in param the host and ports
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

# take in param the host and ports
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
    exit()

####### Main #######

def main():
    # define the usage command for help
    parser = argparse.ArgumentParser(prog='portsScanner')
    parser.add_argument('-t', '--target', help='specify target host', type=str, required=True)
    parser.add_argument('-r', '--range', help='specifiy target port range seperate by comma (ex: 0,443 -> eq 0 to 443)', type=str)
    parser.add_argument('-a', '--all', help='scann all ports', action='store_true', default=False)
    parser.add_argument('-p', '--port', help='specifiy target port seperate by comma', type=str)
    args = vars(parser.parse_args())
    
    # if option -r used for scan range
    if args['target'] and args['range']:
        tgtHost = args['target']
        tgtRPorts = args['range'].split(',')
        rangePortsScanner(tgtHost, tgtRPorts)

    # if option -a used for scan all 65536 ports
    if args['target'] and args['all'] == True:
        tgtHost = args['target']
        multiPortsScanner(tgtHost)

    # else scan specifics ports in -p <port>,<port>
    if args['target'] and args['port']:
        tgtHost = args['target']
        tgtPort = args['port'].split(',')
        portScanner(tgtHost, tgtPort)

# main function
if __name__ == '__main__':
    main()