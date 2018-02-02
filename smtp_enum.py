#!/usr/bin/python
import socket
import sys
import ipaddress
import getopt

def main(argv):
   ipaddr = ''
   filepath = ''
   try:
      opts, args = getopt.getopt(argv,"hf:i",["file=","ip="])
   except getopt.GetoptError:
      print 'smtp_enum.py -f <file> -i <ipaddress>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'smtp_enum.py -f <file> -i <ipaddress>'
         sys.exit()
      elif opt in ("-f", "--file"):
         filepath = arg
      elif opt in ("-i", "--ip"):
         ipaddr = arg
   print 'ip address is %s' % ipaddr
    # Create a Socket
   s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the Server
   connect=s.connect((ipaddr,25))
    # Receive the banner
   banner=s.recv(1024)
   print banner


   with open(filepath) as fp:  
      for cnt, line in enumerate(fp):

      	s.send('VRFY ' + line + '\r\n')
      	result=s.recv(1024)
      	print result
      	print("Line {}: {}".format(cnt, line))
    # Close the socket
   s.close()

if __name__ == "__main__":
   main(sys.argv[1:])


