#!/usr/bin/env python3

### "gpsbabel -w -r -t -i gpx \
#	-f /Users/acd/Downloads/doctechniquertsl/2022-09-22 NoUADHIBOU - SaINT-LOUIS.gpx \
#	-f /Users/acd/Downloads/doctechniquertsl/2022-09-21 Cap Juby Tarfaya - LAAYOUNE  Hassan 1er.gpx \
#		-o kml -F freak.kml 
### 

import glob
from datetime import datetime
import os

filz = glob.glob('*.gpx')

command = "gpsbabel -w -r -t -i gpx {input}"
for f in filz:
    command = command.format(input="-f '" + f+"' {input}")
command = command.format(input=' -o kml -F ' + 'RTSL_' + datetime.today().strftime('%Y-%m-%d') + '.kml')
os.system(command)

    
    
