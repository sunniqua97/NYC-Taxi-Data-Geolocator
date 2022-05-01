
# Parse the csv for all the appropriate data fields
import sys
import shapely.wkt
import csv
from shapely.geometry import MultiPolygon, Polygon
from geojson import MultiPolygon
from shapely import wkt
from shapely.geometry import Point, Polygon


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




# 2D array containing [locationID, MULTIPOLYGON coordinates]

f = open('taxi_zones (4).csv','r')
reader = csv.reader(f)
taxi_zones = []

for row in reader:
    #pickup long/lat, dropoff long/lat
    taxi_zones.append([row[0], row[1]])




# function to convert the longitude and latitude to a Point value

def createPoint(p1,p2):
    testPoint = Point(float(p1),float(p2))

#function to search for point locationID based on longitude, latitude input

def returnLocationID(p1,p2):

    #default value incase point isn't found in locationID table
    ans = "NA"

    #convert the longitude and latitude to a Point value
    testPoint = Point(float(p1),float(p2))


    i = 1 #ignore the first row that contains the headers

    #checking through each multipolygon in the taxizones
    for MULTIPOLYGON in taxi_zones:
        if(ans != "NA"):
            break
        if (i==0):
            multiWKT = shapely.wkt.loads(MULTIPOLYGON[1])

            #parsing through each polygon in the MULTIPOLYGON
            for polygon in multiWKT:

                #check if the point is found within a polygon, then return the locationID
                if(testPoint.within(polygon)):
                    #print(polygon)
                    #print("FOUND")
                    ans = (MULTIPOLYGON[0])
                    break

        else:
            i = i - 1

    return ans



#testing the returnLocationID
#long_A = '-73.990371704101563'
#lang_A = '40.734695434570313'

#long_B = '-74.01299294779471'
#lang_B = '40.71029311630474'

#returnLocationID(long_B,lang_B)


#filename file must be formatted to only include pickup long/lat, dropoff long/lat
#if your file is not in that format, function will not work


def createLocationArray(filename):
    f = open(filename,'r')
    reader = csv.reader(f)


    taxi_data = []
    for row in reader:
        #pickup long/lat, dropoff long/lat
        taxi_data.append([row[0], row[1], row[2], row[3]])
        #print(taxi_data[-1])

    #store the final 2D array to create the newLocationID file
    final_taxi_data = []

    counter = 1 #ignore the first row that contains the headers
    for taxi_location in taxi_data:
        if (counter == 0):
            #print(returnLocationID(taxi_location[0],taxi_location[1]))
            #print(returnLocationID(taxi_location[2],taxi_location[3]))
            final_taxi_data.append([(returnLocationID(taxi_location[0],taxi_location[1])),(returnLocationID(taxi_location[0],taxi_location[1]))])
            #print(final_taxi_data[-1])
        else:
            counter = counter - 1
            final_taxi_data.append(["PICKUP LOCATION ID", "DROP OFF LOCATION ID"])
            #print(final_taxi_data[0])


A = 'yellow_tripdata_2010-10.csv'
createLocationArray(A)

#def fileConversion


#save the 2D array containing [locationID, POLYGON coordinates] to a csv
#with open('final_taxi_zones.csv','w',newline='') as f:
#    writer = csv.writer(f)
#    writer.writerows(taxi_zones)

#parse the  MULTIPOLYGON by list of POLYGONS

#test case for the point being found
#p1 = Point(-74.01299294779471, 40.71029311630474)


#i = 1 #ignore the first row that contains the headers
#for MULTIPOLYGON in taxi_zones:
#    if (i==0):
#        multiWKT = shapely.wkt.loads(MULTIPOLYGON[1])
#        #parsing through each polygon
#        for polygon in multiWKT:

#            #check if the point is found within a polygon, then return the polygon, locationID, and FOUND
#            if(p1.within(polygon)):
#                print(polygon)
#                print("FOUND")
#                print(MULTIPOLYGON[0])
#        #polygonList = list(multiWKT)
#        #print(polygonList[0])
#    else:
#        i = i - 1



#import csv
#import pandas as pd
#from shapely.geometry import Point
#from shapely.geometry.polygon import Polygon
#import shapely.wkt



#f = open('manhattan taxi zones.csv','r')
#reader = csv.reader(f)


#taxi_zones = []
#for row in reader:
    #pickup long/lat, dropoff long/lat
#    taxi_zones.append([row[0], row[2]])

#print(taxi_zones[2])



#preprocessing
#clean up the data to have it cleanly in a list


#key_list = list(locationData.keys())
#val_list = list(locationData.values())

#for i in range(len(val_list)):
#    val_list[i] = ((val_list[i].replace("'","")).replace(",",""))
#   val_list[i] = val_list[i].split(" ")
#    print (val_list[i])

#searches the 2D list for the proper lat/long value pair
#takes values as a string

#def findLocation(longit,latit):
 #   for i in range(len(val_list)):
  #      for k in range(len(val_list

#f = open('file3.csv','r')
#reader = csv.reader(f)


#people = []
#for row in reader:
    #pickup long/lat, dropoff long/lat
#    people.append([row[0], row[1], row[2], row[3]])

#for item in people:

#write the new csv with data fields
#with open('file3.csv', 'w', newline='') as f:
#    writer = csv.writer(f)
#    writer.writerows(people)

#print(people[1])


#findLocationtest
#findLocation('-73.94383256699986', '40.78285908899991')
#val_list[0] = ((val_list[0].replace("'","")).replace(",",""))
#print (val_list[0])
#pos = val_list.index('quad')
#print(key_list)
#print(pos)
