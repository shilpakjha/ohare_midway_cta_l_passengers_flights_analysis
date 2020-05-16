# Part 4 - O-Hare L-ridership and passenger volume analysis
# Get the Data 1 and 2 Files Use API to connect with the portal and get with Data 1 and 2
import pandas as pd
import matplotlib.pyplot as plt
import bokeh as bk
import math
from ast import literal_eval

# DataFrame 1
# Get the entire ridership data from 2001 to 2020(Q1)

l_rides = pd.read_csv(
    "https://data.cityofchicago.org/resource/t2rn-p8d7.csv?%24limit=350000"
)
l_rides.head()

# Add date_time, year and month columns to the data set

l_rides["date_time"] = pd.to_datetime(l_rides["month_beginning"])
l_rides["month"] = l_rides["date_time"].dt.month
l_rides["year"] = l_rides["date_time"].dt.year
l_rides.head()

# getting 2014 to 2020 ridership data

l_2014_2020_rides = l_rides[(l_rides["year"] > 2013) & (l_rides["year"] <= 2020)]
l_2014_2020_rides

# DataFrame 2

l_map_stops = pd.read_csv(
    "https://data.cityofchicago.org/resource/8pix-ypme.csv", sep=","
)
l_map_stops

# Use the function to create the x and y coordinates for each l-stop
# Add the co-ordinates to each L-stop
# Merc function created by Colin Patrick Reid used in this code.
def merc(Coords):
    Coordinates = literal_eval(Coords)
    lat = Coordinates[0]
    lon = Coordinates[1]

    r_major = 6378137.000
    x = r_major * math.radians(lon)
    scale = x / lon
    y = (
        180.0
        / math.pi
        * math.log(math.tan(math.pi / 4.0 + lat * (math.pi / 180.0) / 2.0))
        * scale
    )
    return (x, y)


l_map_stops["coords_x"] = l_map_stops["location"].apply(lambda x: merc(x)[0])
l_map_stops["coords_y"] = l_map_stops["location"].apply(lambda x: merc(x)[1])
l_map_stops[["location", "coords_x", "coords_y"]].head()

# Drop duplicates since each stop is for going to and going from directions. ALl other data stays same.
l_map_stops.drop_duplicates(subset="map_id", keep="last", inplace=True)

# Change the column name "map_id" to match the name in the l_2014_2020_rides column name which is "station_id"
# This will allow us to merge DataFrames 1 and 2
# The new merged dataframe wnow contains the line infor added for each station.
l_map_stops.rename(columns={"map_id": "station_id"}, inplace=True)
l_map_stops.head()


# Merge the DataFrames 1 and 2 together on the map_id (data)
# This gives us the ridership across all the L-stops between 2014 and 2020.
# Left Joined the ridership data with the L-stop data so that all the ridership rows are included.

merged_rides_lines = pd.merge(
    left=l_2014_2020_rides,
    right=l_map_stops,
    how="left",
    left_on="station_id",
    right_on="station_id",
)

# Sort the monthtotal values in ascending order

merged_rides_lines.sort_values(ascending=False, by="monthtotal", inplace=True)
# Filled the na rows and columns with their corresponding values as in the ridership datafile
merged_rides_lines.stop_id = merged_rides_lines.stop_id.fillna(0)
merged_rides_lines.stop_name = merged_rides_lines.stop_name.fillna("noname")
merged_rides_lines.direction_id = merged_rides_lines.direction_id.fillna("noname")
merged_rides_lines.station_name = merged_rides_lines.station_name.fillna("noname")
merged_rides_lines.station_descriptive_name = merged_rides_lines.station_descriptive_name.fillna(
    "noname"
)
# ada column converted to datatype object since na values filled as "noname"
merged_rides_lines.ada = merged_rides_lines.ada.fillna("nodata")
merged_rides_lines.pnk = merged_rides_lines.pnk.fillna(True)
merged_rides_lines.brn = merged_rides_lines.brn.fillna(True)
merged_rides_lines.g = merged_rides_lines.g.fillna(True)
merged_rides_lines.o = merged_rides_lines.o.fillna(True)
merged_rides_lines.p = merged_rides_lines.p.fillna(True)
merged_rides_lines.red = merged_rides_lines.red.fillna(False)
merged_rides_lines.blue = merged_rides_lines.blue.fillna(False)
merged_rides_lines.pexp = merged_rides_lines.pexp.fillna(False)
merged_rides_lines.y = merged_rides_lines.y.fillna(False)

merged_rides_lines

# O-Hare and Midway ridership between 2014 to 2020

aiport_2014_to_2020_rides = merged_rides_lines[
    merged_rides_lines["stationame"].isin(["O'Hare Airport", "Midway Airport"])
]
aiport_2014_to_2020_rides

# O'hare airport 2019 L-rides by month
airports_sub_rides = aiport_2014_to_2020_rides.groupby(
    ["stationame", "year", "month"]
).sum()
airports_sub_rides
airports_sub_rides.sort_values(ascending=True, by="stationame", inplace=True)
df10 = pd.pivot_table(
    data=airports_sub_rides,
    index=["stationame", "year", "month"],
    values=["monthtotal"],
    aggfunc="sum",
).reset_index()
df11 = df10[df10["year"].isin(["2019"])].copy()
df12 = df11[df11["stationame"].isin(["O'Hare Airport"])]
df13 = df12.copy()
df13.sort_values(ascending=False, by="monthtotal", inplace=True)
df13.rename(columns={"monthtotal": "ohare_l_monthtly_rides"}, inplace=True)
df13
