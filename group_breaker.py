from AppKit import NSPasteboard, NSStringPboardType
import pyperclip as pc

pb = NSPasteboard.generalPasteboard()
pbstring = pb.stringForType_(NSStringPboardType)

tab_count_forward = 1
tab_count_backward = pbstring.count(")")

new_pb_string = ""
num_of_tabs = "\t"

for char_ in pbstring:
    if char_ == "(":
        num_of_tabs = tab_count_forward * '\t'
        new_pb_string += "\n" + num_of_tabs + "(\n" + num_of_tabs + "\t"
        tab_count_forward += 1
    
    elif char_ == ")":
        tab_count_forward = tab_count_forward - 1
        num_of_tabs = tab_count_forward * '\t'
        new_pb_string += "\n" + num_of_tabs + ")\n" + num_of_tabs + "\t"

    else:
        new_pb_string += char_

pc.copy(new_pb_string)