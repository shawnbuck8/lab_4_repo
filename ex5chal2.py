import arcpy
from arcpy import env
env.workspace = "J:/EsriPress/Python/Data/Exercise05"
arcpy.management.AddXY("hospitals.shp")
print "I've added xy points to hospitals!"


