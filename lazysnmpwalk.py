#!/usr/bin/python
import sys
import getopt
from subprocess import call
def main(argv):
   ipaddr = ''
   filepath = ''
   try:
      opts, args = getopt.getopt(argv,"hf:",["file="])
   except getopt.GetoptError:
      print 'lazysnmpwalk.py -f <file>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'lazysnmpwalk.py -f <file>'
         sys.exit()
      elif opt in ("-f", "--file"):
         filepath = arg
   f = open(filepath)
   for line in iter(f):

   	call(["snmpwalk", "-c public", "-v1", line])
   	call(["snmpwalk", "-c public", "-v1", line, "1.3.6.1.2.1.25.1.6.0"])
	call(["snmpwalk", "-c public", "-v1", line, "1.3.6.1.2.1.25.4.2.1.2"])
	call(["snmpwalk", "-c public", "-v1", line, "1.3.6.1.2.1.25.4.2.1.4"])
	call(["snmpwalk", "-c public", "-v1", line, "1.3.6.1.2.1.25.2.3.1.4"])
	call(["snmpwalk", "-c public", "-v1", line, "1.3.6.1.2.1.25.6.3.1.2"])	
	call(["snmpwalk", "-c public", "-v1", line, "1.3.6.1.4.1.77.1.2.25"])
	call(["snmpwalk", "-c public", "-v1", line, "1.3.6.1.2.1.6.13.1.3"])
   f.close()
if __name__ == "__main__":
   main(sys.argv[1:]) 

