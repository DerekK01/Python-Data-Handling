
import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd

#Input file
myhouse_file = open('myhouse.csv')

#Seperation
myhouse_string = myhouse_file.read()
device_data = myhouse_string.split("\n",1)[1]
residents = myhouse_string.split("\n",1)[0].split(":")[1]
print(device_data)
print(residents)
amount_of_devices = device_data.count('\n') + 1
print(amount_of_devices)


device_list = device_data.replace(':',',').replace('\n',',').split(',')

device_array = np.array(device_list).reshape(amount_of_devices,26)
print(device_array)



#putting the data in to array
add_array = []
add_array2 = []
add_device = []
add_totalpower = []
add_hour = []
for i in range(amount_of_devices):
    total_device_usage = 0
    for x in range(24):
        total_device_usage += float(device_array[i,x+2])
        
    #For Array [Device,Power,Hr]    
    add_array.append(device_array[i,0])
    add_array.append(device_array[i,1])
    add_array.append(total_device_usage)
    
    #For Array [Device,Power*Hr]    
    add_array2.append(device_array[i,0])
    add_array2.append(int(float(device_array[i,1]) * total_device_usage))
    
    #For Array [Device]
    add_device.append(device_array[i,0])
    
    #For Array [Power*Hr]
    add_totalpower.append(float(device_array[i,1]) * total_device_usage)
    
    #For Array [Hour]
    add_hour.append(total_device_usage)




device_power_df = pd.DataFrame({'Device' : add_device,'Total_Power' : add_totalpower})

sorted_device_power_df= device_power_df.sort_values(by=['Total_Power'])
print(sorted_device_power_df)


#Plotting the first graph
sorted_device_power_df.plot.barh(x='Device',y='Total_Power',title='Device Power Usage In A Day').set(xlabel='Total Power used (Watt * Hr)',ylabel='Device')
plt.style.use = 'default'
plt.tight_layout()
plt.legend(loc="right", fancybox=True, shadow=True)
plt.savefig("Device power usage in a day.png")
plt.show()




#Plotting second graph
plt.xlabel('Device')
plt.ylabel('Hour used')
plt.title('Times used for each device')
plt.bar(add_device,add_hour)
plt.xticks(rotation=80)
plt.tight_layout()
plt.savefig("Times used for each device.png")
plt.show()


#sum vertically 
power_per_hour_array = []
time_array=["12:00AM","1:00AM","2:00AM","3:00AM","4:00AM","5:00AM","6:00AM","7:00AM","8:00AM","9:00AM","10:00AM","11:00AM","12:00PM","1:00PM","2:00PM","3:00PM","4:00PM","5:00PM","6:00PM","7:00PM","8:00PM","9:00PM","10:00PM","11:00PM",]
for i in range(24):
    total_usage_per_hour = 0
    for x in range(amount_of_devices):
        total_usage_per_hour += float(device_array[x,1]) * float(device_array[x,i+2])
    
    #For Array [Power Per Hour]
    power_per_hour_array.append(total_usage_per_hour)
    

#Plot the third graph
print(power_per_hour_array)
plt.xlabel('Hour')
plt.ylabel('Power Usage')
plt.title('Power used per hour')
plt.plot(time_array,power_per_hour_array)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("power used per hour.png")
plt.show()    


    


myhouse_file.close()    

