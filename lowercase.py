#!/usr/bin/env python
from AppKit import NSPasteboard, NSStringPboardType
import pyperclip as pc
 
pb = NSPasteboard.generalPasteboard()
pbstring = pb.stringForType_(NSStringPboardType)
 
pc.copy(pbstring.lower())