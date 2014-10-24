import arcpy

from arcpy import env
env.overwriteOutput = True
env.workspace = "J:/EsriPress/Python/Data/Exercise07"
fc = "Results/airportsCopy.shp"
qry1 = "\"FEATURE\" = 'Airport'"
qry2 = "\"FEATURE\" = 'Seaplane Base'"
arcpy.Select_analysis(fc, "Results/airports_int.shp", qry1)
arcpy.Select_analysis(fc, "Results/Seaplane_int.shp", qry2)
arcpy.analysis.Buffer("Results/airports_int.shp", "Results/airports_buffer_final", "15000 METERS")
print "Created Airport's Buffer Layer!"
arcpy.analysis.Buffer("Results/Seaplane_int.shp", "Results/Seaplane_buffer_final", "7500 METERS")
print "Created Seaplane Base Buffer Layer!"
    
print "Done!"


