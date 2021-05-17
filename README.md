# enginemonitor

## Overview

### Installation

via Source
```
$ git clone https://github.com/BennyCarbajal/enginemonitor
$ pip install .
```

### Examples

via Execute: You have to run as administrator
```
from enginemonitor import Engine
import json

ngin = Engine()

out = json.dumps( {
 'cpu': ngin.getCpu(),
 'sensors': ngin.getSensorBySpecs( "CPU", "Temperature" )
}, indent=2 )

print( out )
```

via Service: You need to install MongoDB and run GarboMonitorService.exe as administrator on your computer. It`s fastest this via.
```
from enginemonitor import Engine
import json

ngin = Engine()

out = json.dumps( {
 'cpu': ngin.getCpu(),
 'sensors': ngin.getMonitorServiceBySpecs( "CPU", "Temperature" )
}, indent=2 )

print( out )
```