import json
import os
import numpy as np
import pandas as pd
import requests as req

request_countries = req.get('http://api.worldbank.org/v2/countries?format=json').json()


country_list = []
country_info = {}
iso_codes = []
name = []


for i in range(1, 7):
    request_country_iso = req.get("http://api.worldbank.org/v2/countries?format=json&page=%s" %(i)).json()
    country_list.append(request_country_iso)

for i in range(len(country_list)):
    for j in range(0, 49):
        iso_codes.append(country_list[i][1][j]['iso2Code'])
        name.append(country_list[i][1][j]['name'])


country_info = dict(zip(name, iso_codes))

country = input("What country are you looking for?")

#def wb_find_data(country):
for name, iso_codes in country_info.items():
    if country == name:
        ref = iso_codes
        request = req.get("http://api.worldbank.org/v2/countries/%s/indicators/DT.ODA.ODAT.CD?format=json" %(ref)).json()
        for i in range(0, 6):
            print("In " + str(request[1][i]['date']) + ", " + str(country) + " had " + str(request[1][i]['value']) + " in net official development assistance received (Current US$).")
                #print(request[1][i]['value'])
