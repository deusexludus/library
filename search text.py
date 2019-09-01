'''
Bruce Dunn 
Python 3.7
Searches an array of filenames for an array of strings and prints a message if a match is found.
bytearrays are used so only works for ASCII files
copy the files to the same folder as the script
'''
import mmap

filenames=[
    'GEN_TM_EMB.m',\
    'GEN_N2_IDLE_UPTRIM_EMB.m',\
    'GEN_TM_EMB_ADDL.m',\
    'GEN_N1_REVMAX_EMB.m',\
    'GEN_SBV_EMB.m',\
    'GEN_WF_LIMITS_EMB.m',\
    'GEN_N2_N1_IDLE_CONV_EMB.m',\
    'GEN_CSRD_AC27.m',\
    'GEN_SBV_16292.m',\
]

searchstrs=[
    'Figure III-1',\
    'YX320c',\
    'FM041y',\
    'FM200d',\
    'YX077',\
    'YX093',\
    'YX157',\
    'YX185',\
    'YX258',\
    'SB025',\
    'TM460d',\
    'TM470f',\
    'JR160a',\
    'LIB03',\
    'LIB07',\
    'LIB12a',\
    'DF120',\
    'JR179',\
    'JR525k',\
    'JR565d',\
    'JR605d',\
    'FM040n',\
    'AR550p',\
    'FM130',\
    'FM150h',\
    'FM160g',\
    'FM170g',\
    'FM230n',\
    'FM370',\
    'JR418k',\
    'JR424c',\
    'TM390e',\
    'TM392d',\
    'TM602d',\
    'XE100',\
    'YX380h',\
    'XC100e',\
    'YX255b',\
    'TM350c',\
    'FM210i',\
    'TM390e',\
    'TM392d',\
    'MC170',\
    'YX242e',\
    'YX246a',\
    'YX248a',\
    'YX250d',\
    'JR150a',\
    'MC097a',\
    'MC161p',\
    'YX140b',\
    'MC057b',\
    'JR111c',\
    'SB011e',\
    'YX194c',\
    'YX217e',\
    'AR544e',\
    'LIB16a',\
    'Label 325',\
    'Label 326',\
    'LABEL 325',\
    'LABEL 326',\
    'JR565d',\
    
#    'disp', #ensures the script is working\
]    

print('Starting...')
for i in range(len(filenames)):
    with open(filenames[i], 'rb', 0) as file,\
         mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
        for searchstr in searchstrs:
            b = bytearray()
            b.extend(map(ord, searchstr))
            if s.find(b) != -1:
                print('found',searchstr,'in',filenames[i])
        print('Finished file',filenames[i])
print('Done!')