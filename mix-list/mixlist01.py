#!/usr/bin/env python3

# Creates a List
my_list = [ "192.168.0.5", 5060, "UP" ]

# Pints first item
print("The first item in the list (IP): " + my_list[0] )
    
# Prints second item
print("The second item in the list (port): " + str(my_list[1]) )
    
# Prints third item
print("The last item in the list (state): " + my_list[2] )


iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print( "IP addresses: " , iplist[3], " and ", iplist[4])
