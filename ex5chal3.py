import arcpy
from arcpy import env
env.workspace = "J:/EsriPress/Python/Data/Exercise05"
arcpy.management.Dissolve("parks.shp", "Results/parks_dissolve.shp", "PARK_TYPE", "", "SINGLE_PART", "")
print arcpy.GetMessages()
print "I've dissolved the parks shapefile!"


