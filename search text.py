'''
Python 3.7
Searches an array of filenames for an array of strings and prints a message if a match is found.
bytearrays are used so only works for ASCII files
copy the files to the same folder as the script
'''
import mmap
import os
import re

def getFileNames():
#this method prints the filenames in a folder (including all subfolders)
#use "r" before filename to use normal string, or escape "\" with "\" or use "/"
    for root, dirs, files in os.walk(r"C:\Users\H116099\Documents\archive\python\search TID"):
        for filename in files:
            print("'",filename,"\',\\")
#getFileNames()

filenames=[
    'AllTestIds_0830_0940_ARINC_DISCRETES.py',\
    'AllTestIds_0830_0957_TLD_Single.py',\
    'AllTestIds_0830_0943_ARINC.py',\
    'AllTestIds_0830_0956_TR.py',\
    'AllTestIds_0830_0952_ECFR_Events.py',\
    'AllTestIds_0830_0954_GenOps.py',\
    'AllTestIds_0830_0953_Exceedances.py',\
    'AllTestIds_0830_0956_FD.py',\
    'AllTestIds_0830_0942_ECFR.py',\
    'AllTestIds_0830_0955_SigSel.py',\
    'AllTestIds_0830_0958_Start_SD.py',\
    'AllTestIds_0830_0959_TLD_Dual.py',\
    'AllTestIds_0830_0942_TM.py',\
    'AllTestIds_0830_0952_ECFR_Incidents.py',\
]
"""
searchstrs=[
    'MSJ',\
    'MLJ',\
    'SMS',\
    'fl_eng_sms',\
    'fl_eng_mlj',\
    'fl_eng_msj',\
    'A_ENG_ID1',\
    'A_ENG_ID2',\
    'A_ENG_ID3',\
    'A_ENG_ID4',\
    'A_ENG_ID5',\
    'A_ENG_ID6',\
    'A_ENG_ID7',\
    'A_ENG_ID8',\
    
#    'disp', #ensures the script is working\
]    
"""
searchstrs=[
    'aircraft type',\
    'SeteNgid']

class Searches:
    
    def searchWrapper(self, filenames, searchstrs):
        #interactive, choose type of search
        stype=input("type b for bytesearch and r for regexp: ")
        print('starting %s' %stype)
        for i in range(len(filenames)):
            if stype=="b":
                self.byteSearch(filenames[i], searchstrs)
            if stype=='r':
                self.regExpSearch(filenames[i], searchstrs)
            print('Finished file',filenames[i])
        print('Done!')
        
    def byteSearch(self, filename, searchstrs):
        #bytearrays are used so only works for ASCII files
        #capitalization matters!! Because of bytearray.
        with open(filename, 'rb', 0) as file,\
             mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
            for searchstr in searchstrs:
                b = bytearray()
                b.extend(map(ord, searchstr))
                if s.find(b) != -1:
                    print("found",searchstr,'in',filename)
                    
    def regExpSearch(self, filename, searchstrs):
            for j, line in enumerate(open(filename)):
                for searchstr in searchstrs:
                    for match in re.finditer(searchstr, line,re.I or re.M): 
                        #re.I and re.M modifiers make search insensitive to capitalization and multiline
                        print('Found on line %s: %s' % (j+1, match.group()))        

s=Searches()
s.searchWrapper(filenames, searchstrs)
