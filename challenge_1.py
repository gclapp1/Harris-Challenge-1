# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE
#Grayson Clapp

# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy 
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020 
# to analyze supply and demand for bikes in the system. 

# NOTE ** if you aren't able to run this, type "pip install json" into your command line
import json

# do not delete; this is the data you'll be working with

divvy_stations = json.loads(open('divvy_stations.txt').read())

##SOURCE: https://www.geeksforgeeks.org/python-get-values-of-particular-key-in-list-of-dictionaries/

# PROBLEM 1
# find average number of empty docks (num_docks_available) and 
# available bikes (num_bikes_available) at all stations in the system
avg_empty_docks = sum([sub["num_docks_available"] for sub in divvy_stations])/len(divvy_stations)
avail_bikes = sum([sub["num_bikes_available"] for sub in divvy_stations])


# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system (ignore ebikes)

#currently rented=num_docks_available-num_docks_disabled-num_bikes_disabled-
for a in divvy_stations:
    a= sum([sub["num_docks_available"] for sub in divvy_stations])
    a= a-sum([sub["num_docks_disabled"] for sub in divvy_stations])
    a=a-sum([sub["num_bikes_disabled"] for sub in divvy_stations])
    a=a-sum([sub["num_bikes_available"] for sub in divvy_stations])
    print(a)
    break

ratio_of_bikes=a/sum([sub["num_docks_available"] for sub in divvy_stations])
print('the ratio of bikes currently rented to total bikes in the system is', (ratio_of_bikes), ':1')

# PROBLEM 3 
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows 
# the percentage of bikes available at each individual station (again ignore ebikes). 
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%
for station in divvy_stations:
    x=station['num_bikes_available']
    y=station['num_docks_available']
    z=station["num_docks_disabled"]
    w=station["num_bikes_disabled"]
    if w+x+y+z>0:
        answer=(x/(w+x+y+z))*100
        station.update({'percent_bikes_remaining':round(answer,2)})
    else:
        station.update({'percent_bikes_remaining':'information is corrupted'})

