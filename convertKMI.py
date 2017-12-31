import pygrib
import os

#steeds 36 uren
#http://opendata.meteo.be/geonetwork/srv/dut/catalog.search#/metadata/RMI_DATASET_ALARO


def writeGribMessage(message, wind=False):
    message['generatingProcessIdentifier'] = 96
    message['centre'] = 'kwbc'

    gribout.write(message.tostring())
    if wind:
        gribout_wind.write(message.tostring())
    return

DATADIR = os.path.expanduser("~/PycharmProjects/GribKMI/testdata")
TMPDIR = os.path.join(DATADIR, 'OUTTEST')

lst = []
os.chdir(DATADIR)
for f in os.listdir(os.getcwd()):
    if f.endswith('.grib'):
        lst.append(f)

gribout = open(TMPDIR+'temp.grb', 'wb')
gribout_wind = open(TMPDIR+'temp_wind.grb', 'wb')

for f in lst:
    grbs = pygrib.open(f)
    print(f)
    for grb in grbs:
        param = grb.indicatorOfParameter
        if param == 41:
            #mean sea level pressure
            grb.indicatorOfParameter = 2
            grb.indicatorOfTypeOfLevel = 'sfc'
            grb.typeOfLevel = 'meanSea'
            writeGribMessage(grb)

        elif param == 193:
            #10 m v-wind
            grb.indicatorOfParameter = 33
            writeGribMessage(grb, wind=True)

        elif param == 192:
            #10 m u-wind
            grb.indicatorOfParameter = 34
            writeGribMessage(grb, wind=True)

        elif param == 195:
            #specific humidity
            grb.indicatorOfParameter = 51
            writeGribMessage(grb)

        elif param == 106 or param == 196:
            #relative humidity
            grb.indicatorOfParameter = 52
            writeGribMessage(grb)

        elif param == 107:
            #u-wind on different heights
            grb.indicatorOfParameter = 34
            writeGribMessage(grb)

        elif param == 108:
            #v-wind on different heigths
            grb.indicatorOfParameter = 33
            writeGribMessage(grb)

        elif param == 195:
            #2m dewpoint
            grb.indicatorOfParameter = 17
            writeGribMessage(grb)

        elif param == 200 or param == 98:
            #surface temp or temperature
            grb.indicatorOfParameter = 11
            writeGribMessage(grb)

        elif param == 132:
            #total precipitation
            grb.indicatorOfParameter = 61
            writeGribMessage(grb)

        elif param == 240:
            #cape
            grb.indicatorOfParameter = 157
            writeGribMessage(grb)

        elif param == 102:
            #wet bulb pot temp
            grb.indicatorOfParameter = 13
            writeGribMessage(grb)

        elif param == 198:
            #Tmax
            grb.indicatorOfParameter = 15
            writeGribMessage(grb)

        elif param == 199:
            #Tmin
            grb.indicatorOfParameter = 16
            writeGribMessage(grb)

        elif param == 234:
            #0°C isotherm
            grb.indicatorOfParameter = 141
            writeGribMessage(grb)

msg = 'GRIB file for zyGRIB written!'
print(msg)