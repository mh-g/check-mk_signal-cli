#!/usr/bin/python3
# Send via Signal

import os
from pydbus import SystemBus
from dateutil import parser
from datetime import datetime

eventhostname=os.environ.get ("NOTIFY_HOSTNAME", "<no host>")
eventdatetimeString=os.environ.get ("NOTIFY_LONGDATETIME", "<no time>")
if eventdatetimeString == "<no time>":
    eventdatetime = datetime(2017,1,1)
else:
    eventdatetime = parser.parse (eventdatetimeString)

eventduration=os.environ.get ("NOTIFY_LASTHOSTSTATECHANGE_REL", "<no duration>")
eventhoststate=os.environ.get ("NOTIFY_HOSTSTATE", "<no state>")
eventlasthoststate=os.environ.get ("NOTIFY_LASTHOSTSTATE", "<no last state>")

bus = SystemBus()
signal = bus.get ("org.asamk.Signal")

message = eventhostname + ": " + eventhoststate + " after " + eventlasthoststate + " (" + eventdurati$

signal.sendMessage(message, [], ['+XXXXXXXXXXXXXXXXXXX'])
