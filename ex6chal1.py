import arcpy

from arcpy import env
env.overwriteOutput = True
env.workspace = "J:/EsriPress/Python/Data/Exercise06"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    print fcdesc.basename + " is a " + fcdesc.shapeType + " " + fcdesc.dataType


    
