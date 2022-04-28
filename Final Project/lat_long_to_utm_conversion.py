#importing required libraries and packages
from pandas import *
import pandas as pd
import numpy as np
import utm
import matplotlib.pyplot as plt

#read data from csv file
data = read_csv("morning_stereo_rgb_ir_lidar_gps-vehicle-gps-fix.csv")
latitude=data[".latitude"].astype(float)
longitude=data[".longitude"].astype(float)

#converting into array
latitude=np.array(latitude)
longitude=np.array(longitude)

#converting lat,lon to utm
e,n,z,l=utm.from_latlon(latitude,longitude)
print(e)
print(n)
print(z)
print(l)

#plotting easting and northing
plt.plot(e,n)
plt.xlabel('UTM_EASTING (Meters)') 
plt.ylabel('UTM_NORTHING (Meters)') 
# displaying the title
plt.title("UTM_EASTING VS UTM_NORTHING")
plt.show()

# writing to csv file after conversion
df = pd.DataFrame({"easting" : e, "northing" : n})
df.to_csv('easting_nothing.csv', index=False)
