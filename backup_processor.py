#data_proccessor_2.0.1

# Parse the csv for all the appropriate data fields

import pandas as pd
import numpy as np
import sys
import shapely.wkt
import csv
from shapely.geometry import MultiPolygon, Polygon
from geojson import MultiPolygon
from shapely import wkt
from shapely.geometry import Point, Polygon
#from numba import jit, njit, vectorize
#import time 


#######processing the location data to coordinates map########


#increases the field limits for the csv fields for large MULTIPOLYGONS
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)




# 2D pandas data array containing [locationID, MULTIPOLYGON coordinates(1)]

taxi_zones = pd.read_csv("manhattan zones.csv")






# function to convert the longitude and latitude to a Point value

#def createPoint(p1,p2):
 #   testPoint = Point(float(p1),float(p2))

#createPoint = jit()(createPoint)

#function to search for point locationID based on longitude, latitude input

 #@jit(nopython=True, parallel=True)


manhattan_border_string = "POLYGON((-73.912528 40.796118, -73.921903 40.801776, -73.92766300000001 40.8024, -73.932364 40.80852, -73.933247 40.835632, -73.929128 40.844264, -73.920076 40.85659, -73.913396 40.863342, -73.906769 40.87598100000001, -73.911584 40.87913999999999, -73.915578 40.875696, -73.919855 40.87647, -73.933923 40.882019, -73.952891 40.851198, -73.963639 40.826673, -74.013934 40.757798, -74.023584 40.718157000000005, -74.026382 40.70013500000001, -74.035433 40.685121, -74.019577 40.679654, -74.004043 40.68879, -73.996531 40.701445, -73.9934 40.704633, -73.980909 40.705713, -73.969853 40.709427, -73.967286 40.716938, -73.961722 40.72487, -73.962547 40.736437, -73.96197500000001 40.741297, -73.957017 40.748819, -73.951051 40.754939, -73.941379 40.76709, -73.935903 40.77000099999999, -73.937838 40.774833, -73.934558 40.778251000000004, -73.930038 40.776399, -73.922345 40.780811, -73.90975 40.790954, -73.912528 40.796118))"
manhattan_border = shapely.wkt.loads(manhattan_border_string)
# just returns the locationID of a given coordinate
def returnLocationID(p1,p2,d1,d2):
    testPoint = Point(float(p1),float(p2))
    testPoint2 = Point(float(d1),float(d2))
    
    #default value incase point isn't found in locationID table
    ans = -1
    ans2 = -1
    #testPoint = Point(float(p1),float(p2))

    if (((testPoint.within(manhattan_border)) and (testPoint2.within(manhattan_border)))):
        #checking through each multipolygon in the taxizones
        for MULTIPOLYGON in range(len(taxi_zones)):

            multiWKT = shapely.wkt.loads(taxi_zones.iloc[MULTIPOLYGON][1])
       
            #parsing through each polygon in the MULTIPOLYGON
            for polygon in multiWKT:
                
                #check if the point is found within a polygon, then return the locationID
                if ((ans != -1) and (ans2 != -1)):
                    break
                elif ((ans != -1) and (ans2 == -1)):
                    if(testPoint.within(polygon)):
                        ans2 = (taxi_zones.iloc[MULTIPOLYGON][0])
                
                elif ((ans == -1) and (ans2 != -1)):    
                    if(testPoint.within(polygon)):
                        ans = (taxi_zones.iloc[MULTIPOLYGON][0])
                else:
                    if(testPoint.within(polygon)):
                        ans = (taxi_zones.iloc[MULTIPOLYGON][0])
                        
                    if(testPoint2.within(polygon)):
                        ans2 = (taxi_zones.iloc[MULTIPOLYGON][0])

    
    return str(ans) + " " + str(ans2)




#returnLocationID = njit()(returnLocationID)

#@jit(nopython=True, parallel=True)


def createLocationArray(filename, pickup_long, pickup_lat,dropoff_long,dropoff_lat ):
  

    taxi_data = pd.read_csv(filename, na_values = ['.'], names = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
    #store the final 2D array to create the newLocationID file

    #taxidata_length = taxi_data.size
    
    #final_taxi_data = np.empty((0,taxidata_length),float)
    #empty_array = np.empty((0, 4), int)
    #print(taxi_data.iloc[1][0])

    
    
   # x = 1000
    #t0 = time.time()
    for taxi_location in range(len(taxi_data)):
        #print(taxi_location)
        if (taxi_location != 0):  
            pickup_dropoff_id = returnLocationID(taxi_data.iloc[taxi_location][pickup_long],taxi_data.iloc[taxi_location][pickup_lat],taxi_data.iloc[taxi_location][dropoff_long],taxi_data.iloc[taxi_location][dropoff_lat])
            print(pickup_dropoff_id)
           # x = x-1
            #print(pickup_dropoff_id)
   # t1 = time.time()
    #total_time = t1-t0
    #print(total_time)
        


        
        #final_taxi_data.append([(returnLocationID(taxi_data.iloc[taxi_location][0],taxi_data.iloc[taxi_location][1])),(returnLocationID(taxi_data.iloc[taxi_location][2],taxi_data.iloc[taxi_location][3]))])
        #final_taxi_data = np.append(final_taxi_data, np.array([[pickup_id, dropoff_id]]), axis=0)


#A = 'file3.csv'
#function_jit = jit()(createLocationArray)

A = input("Enter the name of the csv file to process: (filename.csv) ")
createLocationArray(A,5,6,9,10)

