import arcpy

no_ext = "no extensions are available"

if arcpy.CheckExtension("3D") == "Available":
	three_d = "3D Analyst "
else:
	three_d = ""
if arcpy.CheckExtension("Network") == "Available":
	network = "Network Analyst "
else:
	network = ""
if arcpy.CheckExtension("Spatial") == "Available":
	spatial = "Spatial Analyst "
else:
	spatial = ""

print "The following extensions are available: " + three_d + " " + spatial + " " + network + " " + no_ext