# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:01:16 2020

@author: derek
"""

import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd


#===================================================================================================
#Reading the file with pandas

data_powermeter = pd.read_csv("formattedMeter.csv")
print(data_powermeter)


#===================================================================================================
#Plotting the cumilative graph with the Date and time and the Power meter record

#Cumilative graph
data_powermeter.plot(x='Date_and_time',y='Power_meter',color='red',title='Power meter accumulated',label='Power meter').set(xlabel='Date and Time',ylabel='Power Meter')
plt.style.use = 'seaborn'
plt.xticks(data_powermeter.index, data_powermeter['Date_and_time'], rotation=90)
plt.tight_layout()
plt.savefig("Cumilative_graph.png")


#===================================================================================================
#Plotting the power usage graph 

#Non cumulative graph
data_powermeter['differences'] = data_powermeter['Power_meter'].diff() #To get the differences of the cummulative values
print(data_powermeter)
data_powermeter.plot(kind='line',x='Date_and_time',y='differences',color='red',title='Power meter used',label='Power meter').set(xlabel='Date and Time',ylabel='Power Meter')
plt.style.use = 'seaborn'
plt.xticks(data_powermeter.index, data_powermeter['Date_and_time'], rotation=90)
plt.tight_layout()
plt.savefig("Non_Cumilative_graph.png")


#===================================================================================================
#Create a graph for everyday and observe the difference of the power usage each day.

#each day graph
data_powermeter['Date']=pd.to_datetime(data_powermeter['Date_and_time']).dt.date
data_powermeter['Time']=pd.to_datetime(data_powermeter['Date_and_time']).dt.time
print(data_powermeter)

#title = the date  | data_group = data for each day |  .groupby = group all the duplicate date
for title, date_group in data_powermeter.groupby('Date'):
    text = 'Power usage on ' +str(title)
    date_group.plot(x='Time', y='differences', title=text,color='orange',label = 'Power Usage')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(text +'.png')

