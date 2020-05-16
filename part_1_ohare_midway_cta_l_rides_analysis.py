# May 15, 2020 O'Hare, Midway rides, flights and passenger volume analysis.
# Part 1 - Get data using API
# Use API to connect with the portal to get the data
import pandas as pd
import matplotlib.pyplot as plt
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

# Grouping the rides by airports from 2014 to 2020

airports_sub_rides = aiport_2014_to_2020_rides.groupby(["stationame", "year"]).sum()

airports_sub_rides.sort_values(ascending=True, by="stationame", inplace=True)
airports_sub_rides
df2 = pd.pivot_table(
    data=airports_sub_rides,
    index=["stationame", "year"],
    values=["monthtotal"],
    aggfunc="sum",
).reset_index()
df3 = df2[df2["year"].isin(["2014", "2015", "2016", "2017", "2018", "2019"])].copy()
df4 = df3[df3["stationame"].isin(["O'Hare Airport", "Midway Airport"])]
df4

df5 = pd.pivot_table(
    data=df4, index=["stationame"], columns=["year"], values="monthtotal"
).reset_index()
df5["percent_diff_2016_2019"] = (df5[2019] - df5[2016]) * 100 / df5[2016]
df5.sort_values(ascending=False, by="percent_diff_2016_2019", inplace=True)
# L-Ridership grouped by airport and year(2014-2019)
df5
# Change the values to comma and percent format.
# The datatypes of these column values are now objects and not numbers
df5[2014] = df5[2014].astype(int).apply(lambda x: "{:,}".format(x))
df5[2015] = df5[2015].astype(int).apply(lambda x: "{:,}".format(x))
df5[2016] = df5[2016].astype(int).apply(lambda x: "{:,}".format(x))
df5[2017] = df5[2017].astype(int).apply(lambda x: "{:,}".format(x))
df5[2018] = df5[2018].astype(int).apply(lambda x: "{:,}".format(x))
df5[2019] = df5[2019].astype(int).apply(lambda x: "{:,}".format(x))
df5["percent_diff_2016_2019"] = (
    df5["percent_diff_2016_2019"].astype(float).apply(lambda x: "{:.2f}%".format(x))
)
df5
# Select data for 2016 and 2019 and give the percent diff between 2016 and 2019 rides
df6 = df5[["stationame", 2016, 2019, "percent_diff_2016_2019"]]
df6
