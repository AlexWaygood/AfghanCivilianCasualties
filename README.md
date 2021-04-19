# AfghanCivilianCasualties

This repository contains the code and data I used to create this Flourish interactive visual: https://public.flourish.studio/visualisation/5894019/.

The problem was: I wanted to create a province-by-province map of 2020 civilian casualties in Afghanistan. I could download detailed data on civilian casualties from Action on Armed Violence, but they didn't break down incidents by province. However, they did provide a detailed description of each incidence of violence. In many cases, these had the province name in the description. In many other cases, these had the district name in the description, from which the province could be inferred.

AOAV_Afghan_casualty_2020_data.csv is data originally downloaded from Action on Armed Violence's database here: http://www.explosiveviolencedata.com/filters

AfghanDistricts.csv is a district-lookup database I created by concatenating the several lookup databases found on this site: https://www.arcgis.com/apps/MapSeries/index.html?appid=8d899b0f5b29476c9ca356c0484694c6

AfghanDistricts.txt is a textfile version of all the possible district names listed in AfghanDistricts.txt.

Infer_Province.py is the script I ran to infer the province for all violent incidents listed in AOAV_Afghan_casualty_2020_data.csv.

Cleaned_AOAV_Data.csv is the spreadsheet, with violent incidents broken down province-by-province, that the script spits out. All I then needed to do was to create a Pivot Table in Excel, and paste the data into Flourish.
