#! /usr/bin/env python

__author__ = "Benny Carbajal"
__copyright__ = "Copyright 2021, ningh"
__credits__ = [ "Benny Carbajal" ]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = [ "Benny Carbajal" ]
__email__ = [ "benny.carbajalb@gmail.com" ]
__status__ = "Beta"

import subprocess, json, socket, psutil, os, wmi
from pymongo import MongoClient

class Engine( object ) :
 """docstring for Info"""
 def __init__( self ):
  self.client = MongoClient( 'mongodb://127.0.0.1:27017' )
  self.db = self.client[ 'machine' ]
  self.conn = wmi.WMI()


 def getSize( self, bytes, suffix = 'B' ) :
  """
  Return the bytes unit and suffix.
  """
  factor = 1024
  for unit in [ '', 'K', 'M', 'G', 'T', 'P' ]:
   if bytes < factor:
    return "{0} {1}{2}".format( bytes, unit, suffix )
   bytes /= factor


 def getIp( self ) :
  """
  Return IP address.
  """
  return socket.gethostbyname( socket.gethostname() )


 def getUser( self ) :
  """
  Return the current username.
  """
  return os.environ.get( 'USERNAME' )


 def getComputer( self ) :
  """
  Return the current computername.
  """
  return os.environ.get( 'COMPUTERNAME' )


 def getCpu( self ) :
  """
  """
  for pr in self.conn.Win32_Processor():
   return pr.Name


 def getCores( self ) :
  """
  """
  out = {
   'PhysicalCores': psutil.cpu_count( logical=False ),
   'TotalCores': psutil.cpu_count( logical=True ),
  }
  return out


 def getRam( self ):
  """
  """
  mem = psutil.virtual_memory()
  return self.getSize(mem.total)


 def getBoard( self ):
  """
  """
  cs = self.conn.Win32_ComputerSystem()[0]
  return cs.Model


 def getGpu( self ):
  """
  """
  out = []
  for vc in self.conn.Win32_VideoController():
   out.append(vc.Name)
  return out


 def getDisks( self ):
  """
  """
  out = []
  for ld in self.conn.Win32_logicaldisk() :
   if ld.DriveType == 3 :
    kind = 'Local Disk'
   elif ld.DriveType == 4 :
    kind = 'Network Drive'
   inside = {
    'divice': ld.DeviceID,
    'type': kind,
    'size': self.getSize( int( ld.Size ) ),
    'free': self.getSize( int( ld.FreeSpace ) ),
    'provider': ld.ProviderName
   }
   out.append( inside )
  return out


 ################################################
 #                By SubProcess                 #
 ################################################


 def getSensorBySpecs( self, hwType, snsrType, filename='bySpecs' ) :
  """
  """
  subprocess.check_output(
   os.path.abspath( os.path.dirname( __file__ ) ) + "\\monitor\\GarboMonitor {0} {1} {2}".format(
    hwType,
    snsrType,
    filename
   ),
   shell = True
  )
  with open( "C:/bin/garbo/log/{}.json".format( filename ) ) as json_file:
   data = json.load(json_file)
   return data


 def getSensorsByHardware( self, hwType, filename='byHardware' ) :
  """
  """
  subprocess.check_output(
   os.path.abspath( os.path.dirname( __file__ ) ) + "\\monitor\\GarboMonitor {0} {1}".format( hwType, filename ),
   shell = True
  )
  with open( "C:/bin/garbo/log/{}.json".format( filename ) ) as json_file:
   data = json.load(json_file)
   return data


 def getSensors( self, filename='sensors' ) :
  """
  """
  subprocess.check_output(
   os.path.abspath( os.path.dirname( __file__ ) ) + "\\monitor\\GarboMonitor {}".format( filename ),
   shell = True
  )
  with open( "C:/bin/garbo/log/{}.json".format( filename ) ) as json_file:
   data = json.load( json_file )
   return data


 ################################################
 #                By Service                    #
 ################################################


 def getMonitorServiceBySpecs( self, hwType, snsrType ) :
  """
  """
  out = { 'name': '', 'type': '', 'sensors': [] }
  try :
   data = list( self.db.hardware.find( { 'type': hwType }, { '_id': 0 } ) )
   for item in data :
    out[ 'name' ] = item[ 'name' ]
    out[ 'type' ] = item[ 'type' ]
    for sensor in item['sensors'] :
     if sensor['type'] == snsrType :
      out['sensors'].append(sensor)
   return out
  except Exception as e :
   return e


 def getMonitorServiceByHardware( self, hwType ) :
  """
  """
  try :
   byHw = list( self.db.hardware.find( { 'type': hwType }, { '_id': 0 } ) )
   return byHw
  except Exception as e :
   return e


 def getMonitorService( self ) :
  """
  """
  try :
   byHw = list( self.db.hardware.find( {}, { '_id': 0 } ) )
   return byHw
  except Exception as e :
   return e