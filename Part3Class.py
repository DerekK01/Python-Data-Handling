
import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd

# This code is basically the same as part2.py except with minor changes for class

class house:
    def __init__(self,myhouse_string):
        device_data = myhouse_string.split("\n",1)[1]
        
        self.residents = myhouse_string.split("\n",1)[0].split(":")[1]
        
        #print(device_data)
        amount_of_devices = device_data.count('\n') + 1
        #print(amount_of_devices)
        device_list = device_data.replace(':',',').replace('\n',',').split(',')
        device_array = np.array(device_list).reshape(amount_of_devices,26)
        #print(device_array)
        
        
        add_device = []
        add_totalpower = []
        add_hour = []
        for i in range(amount_of_devices):
            total_device_usage = 0
            for x in range(24):
                total_device_usage += float(device_array[i,x+2])
    
            #For Array [Device]
            add_device.append(device_array[i,0])
    
            #For Array [Power*Hr]
            add_totalpower.append(float(device_array[i,1]) * total_device_usage)
    
            #For Array [Hour]
            add_hour.append(total_device_usage)
        
        self.deviceLabel = add_device
        self.powerTimesHour = add_totalpower
        self.totalHourForEachDevice = add_hour
        
        
        
        self.hourLabel = ["12:00AM","1:00AM","2:00AM","3:00AM","4:00AM","5:00AM","6:00AM","7:00AM","8:00AM","9:00AM","10:00AM","11:00AM","12:00PM","1:00PM","2:00PM","3:00PM","4:00PM","5:00PM","6:00PM","7:00PM","8:00PM","9:00PM","10:00PM","11:00PM",]
        power_per_hour_array = []
        for i in range(24):
            total_usage_per_hour = 0
            for x in range(amount_of_devices):
                total_usage_per_hour += float(device_array[x,1]) * float(device_array[x,i+2])
            
            #For Array [Power Per Hour]
            power_per_hour_array.append(total_usage_per_hour)
                
        self.powerPerHour = power_per_hour_array
        
        self.totalPower = sum(power_per_hour_array)

