#! /usr/bin/env python

__author__ = "Benny Carbajal"
__copyright__ = "Copyright 2021, ningh"
__credits__ = [ "Benny Carbajal" ]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = [ "Benny Carbajal" ]
__email__ = [ "benny.carbajalb@gmail.com" ]
__status__ = "Beta"

import json
from enginemonitor import Engine

def main() :
 out = json.dumps( {
  'basic': {
   'ip': ngin.getIp(),
   'computername': ngin.getComputer(),
   'username': ngin.getUser(),
   'cpu': ngin.getCpu(), 
   'cores': ngin.getCores(),
   'ram': ngin.getRam(),
   'board': ngin.getBoard(),
   'gpu': ngin.getGpu(),
   'logical_disk': ngin.getDisks()
  },
  'sensors': ngin.getSensorBySpecs( "CPU", "Temperature" )
 }, indent=2 )
 print( out )

if __name__ == '__main__':
 ngin = Engine()
 main()
