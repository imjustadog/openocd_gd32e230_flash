import getpass
import sys
import telnetlib
import struct
import time

HOST = "localhost"
tn = telnetlib.Telnet(HOST,port=4444)
print tn.read_until(">")

filepath = "01_GPIO_Runing_Led.bin"
fb = open(filepath, "rb")
data = fb.read()
bin_word = struct.unpack("<"+str(int(len(data)/4))+"L", data)
for i in range(len(bin_word)):
    command = "mdw phys 0x{:08x}\n".format(i * 4 + 0x08000000)
    tn.write(command)
    data_read = tn.read_until(">")
    data_read = data_read.split(":")[-1].split(">")[0].strip()
    data_bin = "{:08x}".format(bin_word[i])
    if data_read != data_bin:
        print "error! addr:0x{:08x} expect:{} actual:{}".format(i * 4 + 0x08000000, data_bin, data_read)
fb.close()

time.sleep(0.1)

tn.write("exit\n")


