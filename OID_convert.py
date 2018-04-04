# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 21:48:02 2018

@author: a
"""

def notation_OID(oidhex_string):
    
    ''' Input is a hex string and as one byte is 2 charecters i take an 
        empty list and insert 2 characters per element of the list.
        So for a string 'DEADBEEF' it would be ['DE','AD','BE,'EF']. '''
    hex_list = [] 
    for char in range(0,len(oidhex_string),2):
        hex_list.append(oidhex_string[char]+oidhex_string[char+1])
    ''' I have deleted the first two element of the list as my hex string
        includes the standard OID tag '06' and the OID length '0D'. 
        These values are not required for the calculation as i've used 
        absolute OID and not using any ASN.1 modules. Can be removed if you
        have only the data part of the OID in hex string. '''
    del hex_list[0]
    del hex_list[0]
    # An empty string to append the value of the OID in standard notation after
    # processing each element of the list.
    OID_str = ''
    
    # Convert the list with hex data in str format to int format for 
    # calculations.
    for element in range(len(hex_list)):
        hex_list[element] = int(hex_list[element],16)
        
    # Convert the OID to its standard notation. Sourced from code in other 
    # languages and adapted for python.
    x = int(hex_list[0] / 40)
    y = int(hex_list[0] % 40)
    if x > 2:
        y += (x-2)*40
        x = 2;
    OID_str += str(x)+'.'+str(y)
    
    val = 0
    for byte in range(1,len(hex_list)):
        val = ((val<<7) | ((hex_list[byte] & 0x7F)))
        if (hex_list[byte] & 0x80) != 0x80:
            OID_str += "."+str(val)
            val = 0
    
    # print the OID in dot notation.
    print (OID_str)
 
notation_OID('060D2B0621040BA946964812D10905')
    

