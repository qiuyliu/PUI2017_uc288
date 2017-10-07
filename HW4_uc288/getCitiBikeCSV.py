import numpy as np
import os
import sys

# Check if PUIDATA environmental variable exists
if os.getenv("PUIDATA") is None:
    print ("must set PUIDATA env variable")
    sys.exit()

def getCitiBikeCSV(datestring):
    '''
    Retrieves the CitiBike CSV file given a datestring
    and saves it in the directory specified in $PUIDATA
    
    Argument:
        datestring: String in format YYYYMM
    '''
    
    PUIdata = os.getenv("PUIDATA")
    
    print ("Downloading", datestring)
    
    ### First I will check that it is not already there
    if not os.path.isfile(PUIdata + "/" + datestring + "-citibike-tripdata.csv"):
        if os.path.isfile(datestring + "-citibike-tripdata.csv"):
            # if in the current dir just move it
            if os.system("mv " + datestring + "-citibike-tripdata.csv " + PUIdata):
                print ("Error moving file!, Please check!")
                
        #otherwise start looking for the zip file
        else:
            if not os.path.isfile(PUIdata + "/" + datestring + "-citibike-tripdata.zip"):
                if not os.path.isfile(datestring + "-citibike-tripdata.zip"):
                    os.system("curl -O https://s3.amazonaws.com/tripdata/" + datestring + "-citibike-tripdata.zip")
                ###  To move it I use the os.system() functions to run bash commands with arguments
                os.system("mv " + datestring + "-citibike-tripdata.zip " + PUIdata)
            ### unzip the csv 
            os.system("unzip " + PUIdata + "/" + datestring + "-citibike-tripdata.zip")
            ## NOTE: old csv citibike data had a different name structure. 
            if '2014' in datestring:
                os.system("mv " + datestring[:4] + '-' +  datestring[4:] + 
                          "\ -\ Citi\ Bike\ trip\ data.csv " + datestring + "-citibike-tripdata.csv")
            os.system("mv " + datestring + "-citibike-tripdata.csv " + PUIdata)
    
    ### One final check:
    if not os.path.isfile(PUIdata + "/" + datestring + "-citibike-tripdata.csv"):
        print ("WARNING!!! something is wrong: the file is not there!")

    else:
        print ("file in place, you can continue")