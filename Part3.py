
import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd
import Part3Class as Street

#house.deviceLabel             | for each device name
#house.residents               | for the amount of residents
#house.powerTimesHour          | for the Power*Hr
#house.totalHourForEachDevice  | for the total hour each devices used in a day
#house.powerPerHour            | for the total power used in each hour
#house.totalPower              | for the total power of that house each day


#Read the streetInfo.py
time_array=["12:00AM","1:00AM","2:00AM","3:00AM","4:00AM","5:00AM","6:00AM","7:00AM","8:00AM","9:00AM","10:00AM","11:00AM","12:00PM","1:00PM","2:00PM","3:00PM","4:00PM","5:00PM","6:00PM","7:00PM","8:00PM","9:00PM","10:00PM","11:00PM",]
street_define = open('streetInfo.csv')
street_define_read = street_define.read()
amount_of_type = street_define_read.count('\n') + 1
print(amount_of_type)

#Split the data up
street_list = street_define_read.replace('\n',':').split(':')
street_array = np.array(street_list).reshape(amount_of_type,3)
print(street_array[0,1])

house_type = np.empty(amount_of_type,dtype=object)     #  The House Type
house_type_num = np.empty(amount_of_type,dtype=object) #  Amount of each house type


#Pass the file to Part3Class.py
for i in range(amount_of_type):
    house_file = open(street_array[i,1])
    house = house_file.read()
    house_type[i] = Street.house(house)
    house_type_num[i] = street_array[i,2]
    house_file.close()


# Graph for each single House Type
for i in range(amount_of_type):
    type_label = "House Type " + str(i)
    plt.barh(type_label,house_type[i].totalPower)
plt.xlabel('Power Usage (W)')
plt.ylabel('House Type')
plt.title('How much power is used in each single type of house')
plt.savefig("power is used in each single type of house.png")
plt.show()

# Graph for the total number of each house type comparison
for i in range(amount_of_type):
    type_label = "House Type " + str(i) + " (" + str(house_type_num[i]) + ")"
    total_power = float(house_type[i].totalPower) * float(house_type_num[i])
    plt.barh(type_label,total_power)
plt.xlabel('Power Usage (W)')
plt.ylabel('House Type')
plt.title('Total number of each house type comparison')
plt.savefig("Total number of each house type comparison.png")
plt.show()


# Graph for the total number of each house type comparison (PIE)
pie_total_power=[]
pie_label=[]
for i in range(amount_of_type):
    type_label = "House Type " + str(i) + " (" + str(house_type_num[i]) + ")"
    total_power = float(house_type[i].totalPower) * float(house_type_num[i])
    pie_total_power.append(total_power)
    pie_label.append(type_label)

plt.pie(pie_total_power,labels=pie_label,shadow=True,startangle=90,autopct='%1.1f%%')
plt.title('Total power usage of each house type comparison')
plt.legend(loc="center left", bbox_to_anchor=(1, 0, 0, 0), fancybox=True, shadow=True)
plt.tight_layout()
plt.savefig("Total power usage of each house type comparison.png")
plt.show()

# Graph for each single House Type Time coparison
for i in range(amount_of_type):
    type_label = "House Type " + str(i)
    plt.plot(time_array,house_type[i].powerPerHour,label=type_label)
plt.xlabel('Power Usage (W)')
plt.ylabel('Usage')
plt.title('Type of house hour usage')
plt.xticks(rotation=90)
plt.legend(loc=2, bbox_to_anchor=(1.05, 1), fancybox=True, shadow=True)
plt.tight_layout()
plt.savefig("Type of house hour usage")
plt.show()



# Graph for the total number of each house time comparison

for i in range(amount_of_type):
    total_powerperhour = []
    type_label = "House Type " + str(i) + " (" + str(house_type_num[i]) + ")"
    for x in house_type[i].powerPerHour:
        total_powerperhour.append(float(x) * float(house_type_num[i]) )
    plt.plot(time_array,total_powerperhour,label=type_label)
plt.xlabel('Power Usage (W)')
plt.ylabel('Usage')
plt.title('Total Type of house hour usage')
plt.xticks(rotation=90)
plt.legend(loc=2, bbox_to_anchor=(1.05, 1), fancybox=True, shadow=True)
plt.tight_layout()
plt.savefig("Total Type of house hour usage")
plt.show()

# Graph of all house type combined Usage vs Time 

total_street_powerperhour = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(amount_of_type):
    total_powerperhour = []
    type_label = "House Type " + str(i)
    for x in house_type[i].powerPerHour:
        total_powerperhour.append(float(x) * float(house_type_num[i]))
    
    for y in range(24):
        total_street_powerperhour[y] += total_powerperhour[y]
        
plt.plot(time_array,total_street_powerperhour)
plt.xlabel('Power Usage (W)')
plt.ylabel('Usage')
plt.title('Total power used in the street per hour')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("Total power used in the street per hour")
plt.show()

print(house_type[2].totalPower)
print(house_type_num)

