import urllib.request

#urllib.request.urlretrieve(url, file_name)

baseUrl = 'http://opendata.meteo.be//download.php?'
format = 'grib'
type = 'raster'
workspace = 'alaro'
xmin = -0.1415255706207
ymin = 47.379315679724
xmax = 9.2485256906048
ymax = 53.640688592737
bbox = '%s,%s,%s,%s' %(ymin, xmin, ymax, xmax)

layers = ['10_m_u__wind_component',
          '10_m_v__wind_component',
          '2_m_Max_temp_since_ppp',
          '2_m_Min_temp_since_ppp',
          '2_m_dewpoint_temperature',
          '2_m_temperature',
          '2m_Relative_humidity',
          'Convective_rain',
          'Convective_snow',
          'Geopotential',
          'Inst_flx_Conv_Cld_Cover',
          'Inst_flx_High_Cld_Cover',
          'Inst_flx_Low_Cld_Cover',
          'Inst_flx_Medium_Cld_Cover',
          'Inst_flx_Tot_Cld_cover', #checken
          'Large_scale_rain',
          'Large_scale_snow',
          'Mean_sea_level_pressure',
          'Relative_humidity',
          'SBL_Gust',
          'Specific_humidity',
          'Surface_CAPE',
          'Surface_Temperature',
          'Surface_orography',
          'Temperature',
          'Total_precipitation',
          'U-velocity',
          'V-velocity',
          'Vertical_velocity',
          'Wet_Bulb_Poten_Temper',
          'freezing_level_zeroDegC_isotherm']

for lyr in layers:
    url = '{}workspace={}&type={}&layer={}'.format(baseUrl, workspace, type, lyr)
    url += '&format={}&bbox={}'.format(format,bbox)
    print(url)


#'http://opendata.meteo.be//download.php?workspace=alaro&type=raster&layer=10_m_u__wind_component&format=grib&bbox=47.379315679724,-0.1415255706207,53.640688592737,9.2485256906048'