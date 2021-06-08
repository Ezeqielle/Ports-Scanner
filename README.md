# Ports Scanner

[![Python 3.8.5](https://img.shields.io/badge/python-3.8.5-blue.svg)](https://www.python.org/downloads/release/python-385/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/Ezeqielle/Ports-Scanner/blob/master/LICENSE)

First install:
> pip install -r requirement.txt

Commands:
> py portsScanner.py -h

Specific ports scanning:
> py portsScanner.py -t \<host> -p \<ports>

All ports scanning:
> py portsScanner.py -t \<host> -a

Range ports scanning:
> py portsScanner.py -t \<host> -r \<port>,\<port>

For save output in a log file:
> py portsScanner.py -t \<host> -p \<ports> > \<file>.log </br>
> py portsScanner.py -t \<host> -a > \<file>.log </br>
> py portsScanner.py -t \<host> -r \<port>,\<port> > \<file>.log

</br>
</br>
</br>
</br>
© Ezeqielle
</br>
</br>
:warning: **colors don't work all time on windows** :warning:
