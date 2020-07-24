import getpass
import sys
import telnetlib
import struct
import time

HOST = "localhost"
tn = telnetlib.Telnet(HOST,port=4444)
print tn.read_until(">")

time.sleep(0.1)
tn.write("mww phys 0x40022004 0x45670123\n")
print tn.read_until(">")
time.sleep(0.1)
tn.write("mww phys 0x40022004 0xcdef89ab\n")
print tn.read_until(">")
time.sleep(0.1)
tn.write("mww phys 0x40022010 0x01\n")
print tn.read_until(">")
time.sleep(0.1)

filepath = "01_GPIO_Runing_Led.bin"
fb = open(filepath, "rb")
data = fb.read()
bin_word = struct.unpack("<"+str(int(len(data)/4))+"L", data)
for i in range(len(bin_word)):
    command = "mww phys 0x{:08x} 0x{:08x}\n".format(i * 4 + 0x08000000, bin_word[i])
    tn.write(command)
    print tn.read_until(">")
fb.close()

time.sleep(0.1)
tn.write("mww phys 0x40022010 0x0\n")
print tn.read_until(">")
time.sleep(0.1)

tn.write("exit\n")

