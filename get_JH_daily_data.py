import csv
import datetime
import os
import sys
import urllib.request

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = "/data/jh_daily_cases"

start_date = datetime.datetime(2020, 1, 22)

ROOT_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/' \
           'csse_covid_19_data/csse_covid_19_daily_reports/'


i = 0
while True:
    try:
        day_increment = datetime.timedelta(days=i)
        filename = (start_date + day_increment).strftime('%m-%d-%Y') + '.csv'
        urllib.request.urlretrieve(ROOT_URL + filename, ROOT_DIR + DATA_FOLDER + "/" + filename)
        i += 1  # increment counter
    except:
        print("Unexpected error:", sys.exc_info()[0])
        break


#### Process Files

