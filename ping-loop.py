#!/usr/bin/python

import sys, getopt, os, subprocess, multiprocessing.dummy, multiprocessing
from operator import is_not
from functools import partial
def main(argv):
   
   prefix = ''
   begin = ''
   end = ''
   
   try:
       opts, args = getopt.getopt(argv,"p:b:e:",["begin=", "end=", "prefix="])
   except getopt.GetoptError:
      print 'ping-loop.py -p <prefix> -b <begin> -e <end>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print  'ping-loop.py -p <prefix> -b <begin> -e <end>'
         sys.exit()
      elif opt in ("-p", "--prefix"):
         prefix = arg
      elif opt in ("-b", "--begin"):
         begin = arg
      elif opt in ("-e", "--end"):
         end = arg
   def iptable(start, stop, prefix):
       tstop = int(stop) + 1
       prange = range(int(start), tstop)
       iptable = []
       for i in prange:
            iptable.append(str(prefix) + str(i))
       
       return iptable
   def pingLoop(ip):
	try:
		output = subprocess.check_output(['ping', '-c', '1', str(ip)])
		if "Destination host unreachable" in output.decode('utf-8'):
			x = 0 
		elif "Request timed out" in output.decode('utf-8'):
			x = 0
		else:
			return ip
	except subprocess.CalledProcessError:
		x=0

   nthreads = 2 * multiprocessing.cpu_count()
   p = multiprocessing.dummy.Pool(nthreads)
   mytable = iptable(begin, end, prefix)
   output = p.map(pingLoop, mytable)
   dlist = ['None']
   p.close()
   p.join()
   output2 = filter(partial(is_not, None), output)

   print output2
if __name__ == "__main__":
   main(sys.argv[1:])

