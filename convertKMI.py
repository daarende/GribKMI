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


    # try:
    #     # Mean sea level pressure
    #     msg_mslp = grbs.select(indicatorOfParameter=41)
    #     msg_mslp.indicatorOfParameter = 2
    #     msg_mslp.indicatorOfTypeOfLevel = 'sfc'
    #     msg_mslp.typeOfLevel = 'meanSea'
    #     writeGribMessage(msg_mslp)
    # except ValueError:
    #     msg = 'No MSLP in %s' %f
    #     print(msg)

    # # Relative humidity
    # msg_rh = grbs.select(indicatorOfParameter=52)[0]
    # msg_rh.values = msg_rh.values * 100
    # writeGribMessage(msg_rh)
    #
    # # Temperature 2m
    # msg_t = grbs.select(indicatorOfParameter=11)[0]
    # writeGribMessage(msg_t)
    #
    # # U-wind
    # msg_u = grbs.select(indicatorOfParameter=33)[0]
    # writeGribMessage(msg_u, wind=True)
    #
    # # V-wind
    # msg_v = grbs.select(indicatorOfParameter=34)[0]
    # writeGribMessage(msg_v, wind=True)
    #
    # # Precipication Intensity
    # msg_ip = grbs.select(indicatorOfParameter=61, level=456)[0]
    # msg_ip.typeOfLevel = 'surface'
    # msg_ip.level = 0
    # msg_ip.values = msg_ip.values * 3600  # mm/s => mm/h
    # writeGribMessage(msg_ip)
    #
    # # Wind gusts
    # msg_ug = grbs.select(indicatorOfParameter=162)[0]
    # msg_vg = grbs.select(indicatorOfParameter=163)[0]
    # msg_ug.values = sqrt(msg_ug.values ** 2 + msg_vg.values ** 2)
    # msg_ug.indicatorOfParameter = 180
    # msg_ug.typeOfLevel = 'surface'
    # msg_ug.level = 0
    # writeGribMessage(msg_ug, wind=True)