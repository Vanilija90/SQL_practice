import sqlite3
import pandas as pd
db = sqlite3.connect("hubway.db")


def run_query(query):
    return pd.read_sql_query(query, db)

#Query1: How many trips incurred additional fees (lasted longer than 30 minutes)?
query1 = '''
    SELECT COUNT(duration) AS "Trips lasting over 30 min" FROM trips
    WHERE duration > (30*60);
    '''
#Query2: Which bike was used for the longest total time?
query2 = '''
    SELECT bike_number as "Bike", SUM(duration) AS "Duration" FROM trips
    GROUP BY bike_number
    ORDER BY COUNT(bike_number) DESC
    LIMIT 5;
    '''

#Query3: Did registered or casual users take more round trips?

query3 = '''
    SELECT sub_type AS "Subscription", COUNT(*)
    FROM trips, stations 
    WHERE trips.start_station = stations.id
    AND trips.start_station = trips.end_station
    GROUP BY sub_type
    ORDER BY COUNT(*) DESC
    LIMIT 5;
'''

#Query4: Which municipality had the longest average duration?

query4 = '''
    SELECT stations.municipality, AVG(trips.duration)
    FROM trips INNER JOIN stations
    ON trips.start_station = stations.id
    GROUP BY stations.municipality 
    ORDER BY AVG(trips.duration) DESC
    LIMIT 5;
    '''
data = run_query(query4)
print(data)
