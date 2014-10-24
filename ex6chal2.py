import arcpy

from arcpy import env
env.overwriteOutput = True
env.workspace = "J:/EsriPress/Python/Data/Exercise06/Results/NM.gdb/"
arcpy.CreateFileGDB_management("J:/EsriPress/Python/Data/Exercise06/Results", "NM2.gdb")
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    if fcdesc.shapeType == "Polygon":
        arcpy.CopyFeatures_management(fc, "J:/EsriPress/Python/Data/Exercise06/Results/NM2.gdb/" + fcdesc.basename)

print "Done!"


    
