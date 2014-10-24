import arcpy

from arcpy import env
env.overwriteOutput = True
env.workspace = "J:/EsriPress/Python/Data/Exercise07"
fc = "roads.shp"
newfield = "FERRY"
fieldname = arcpy.ValidateFieldName(newfield)
arcpy.AddField_management(fc, fieldname, "TEXT", "", "", 5)
print "New field was added..."
cursor = arcpy.da.UpdateCursor(fc, [newfield, "FEATURE"]
for row in cursor:
                               
    if row[1] == "Ferry Crossing":
        row[0] = "Yes"
    else:
        row[0] = "No"
