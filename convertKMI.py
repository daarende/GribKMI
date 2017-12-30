import pygrib

import os

#steeds 36 uren
#http://opendata.meteo.be/geonetwork/srv/dut/catalog.search#/metadata/RMI_DATASET_ALARO


lst = []
os.chdir(os.path.expanduser("~/PycharmProjects/GribKMI/testdata"))
for f in os.listdir(os.getcwd()):
    if f.endswith('.grib'):
        lst.append(f)

print(f)
print('----')
grbs = pygrib.open(f)
for grb in grbs:
    print(grb.keys())
    print(grb.validDate)
    print(grb.parametersVersion)
    print(grb.parameterName)
    print(grb.parameterUnits)


#for f in lst:
#    print('---------')
#    print(f)
#    print('---------')
#    grbs = pygrib.open(f)
#    for grb in grbs:
#        print(grb)