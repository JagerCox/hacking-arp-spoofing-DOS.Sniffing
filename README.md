# Hacking-arp-spoofing-DOS.Sniffing
## MAC Address souplantation
### Dependencies
dsniff (sudo apt-get install dsniff)
### Attack
```
sudo python arp-spoofing.py <Number 0=DoS, 1=Redirect traffic> <interface> <gateway> <victim>
```
### Example
```
sudo python arp-spoofing.py 1 eth0 192.168.1.1 192.168.1.250
```
