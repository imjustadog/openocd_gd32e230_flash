import getpass
import sys
import telnetlib
import struct
import time

HOST = "localhost"
tn = telnetlib.Telnet(HOST,port=4444)

time.sleep(0.1)
tn.write("mww phys 0x40022004 0x45670123\n")
time.sleep(0.1)
tn.write("mww phys 0x40022004 0xcdef89ab\n")
time.sleep(0.1)
tn.write("mww phys 0x40022010 0x04\n")
time.sleep(0.1)
tn.write("mww phys 0x40022010 0x44\n")
time.sleep(3)
tn.write("mww phys 0x40022010 0\n")
time.sleep(0.1)

tn.write("exit\n")

