# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:35:14 2018

@author: Iva
"""
import json
#import csv

with open ('precipitation.json') as file:
    data = json.load(file)

seattle_list = list()

for item in data:
    if item["station"] == "GHCND:US1WAKG0038":
        #print (item)
        seattle_list.append(item)

precip_monthly_values = [0]*12

    
for item in seattle_list:
    month = int(item['date'][5:7])
    precip_monthly_values[month-1] += item['value']
print(precip_monthly_values)

seattle_yearly = sum(precip_monthly_values)

for item in precip_monthly_values:
    relative_monthly_precip = (item/seattle_yearly)
    print(relative_monthly_precip)

with open('file.json','w') as file:
    json.dump({"Seattle": {"totalYearlyPrecip": seattle_yearly, "totalMonthlyPrecip": precip_monthly_values, "relativeMonthly": relative_monthly_precip}}, file)



        
        
        
        
    
    



    

            
