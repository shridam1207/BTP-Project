# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

table = []
cities = [Ahmedabad, Aizawl, Amaravati, Amritsar, Bengaluru, Bhopal, Brajrajnagar, Chandigarh, Chennai, Coimbatore, Delhi, Ernakulam, Gurugram, Guwahati, Hyderabad, Jaipur, Jorapokhar, Kochi, Kolkata, Lucknow, Mumbai, Patna, Shillong, Talcher, Thiruvananthapuram, Visakhapatnam]

for yy in range(2015,2021):
    for mm in range(1,13):
      for dd in range(1,32): 
        url = "https://airportinfo.live/flight/"+flight+"?d=2019-"+str(mm)+"-"+str(dd)
        url = "https://cpcb.nic.in//upload/Downloads/AQI_Bulletin_" + str(yy)+str(mm)+str(dd)+".pdf"
        req = requests.get(url)
        webp = req.text
        soup = BeautifulSoup(webp, 'html.parser')
        for city in cities:
            City = cities[city]
            Date = url[-10:]
            #duration =(soup.find("span", "duration bold ")).text
            PM25 =(soup.find("span", "PM25")).text
            PM10 = (soup.find("span", "PM10")).text
            NO =(soup.find("span", "bold NO")).text
            NO2 =(soup.find("span", "bold NO2")).text
            NOx = soup.findAll("div","NOx")
            NH3 = (soup.find("span", "NH3")).text
            CO = (soup.find("span", "CO")).text
            SO2 = (soup.find("span", "SO2")).text
            O3 = (soup.find("span", "O3")).text
            Benzene = (soup.find("span", "Benzene")).text
            Toulene = (soup.find("span", "Toulene")).text
            Xylene = (soup.find("span", "Xylene")).text
            AQI = (soup.find("span", "AQI")).text
            AQI_Bucket = (soup.find("span", "AQI_Bucket")).text
            row = []
            row.append(City)
            row.append(Date)
            row.append(PM25)
            row.append(PM10)
            row.append(NO)
            row.append(NO2)
            row.append(NOx)
            row.append(NH3)
            row.append(CO)
            row.append(SO2)
            row.append(O3)
            row.append(Benzene)
            row.append(Toulene)
            row.append(Xylene)
            row.append(AQI)
            row.append(AQI_Bucket)
            row = row + times_text
            table.append(row)

tab_arr = np.array(table)

data = pd.DataFrame(tab_arr, columns = ['City','Date','PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toulene','Xylene','AQI','AQI_Bucket'])
data.to_csv('city_day.csv', index=False, encoding='utf-8')
#data

