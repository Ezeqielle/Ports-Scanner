#!/usr/bin/python3

from socket import *
import optparse
from threading import *
from termcolor import colored, cprint

def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
<<<<<<< Updated upstream
        print(colored(f'[+] {tgtPort}/tcp Open', 'green'))
    except:
        print(colored(f'[-] {tgtPort}/tcp Closed', 'red'))
=======
        result = colored(f'[+] {tgtPort}/tcp Open', 'green')
        print(result)
    except:
        print(f'[-] {tgtPort}/tcp Closed', 'red')
>>>>>>> Stashed changes
    finally:
        sock.close()

def portScanner(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(f'Unknow host {tgtHost}')

    try:
        tgtName = gethostbyaddr(tgtIP)
        print(colored(f'[+] Scan result for: {tgtName(0)}', 'yellow'))
    except:
        print(colored(f'[+] Scan result for: {tgtIP}', 'yellow'))
    
    setdefaulttimeout(1)
    
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target ports>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specifiy target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specifiy target post seperate by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPort == None):
        print(parser.usage)
        exit(0)
    
    portScanner(tgtHost, tgtPort)


if __name__ == '__main__':
    main()