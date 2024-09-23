import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

vehicle_count=np.random.normal(10,30,1440)
random_noise=np.random.random(1440)
total_noise=vehicle_count+random_noise

fs=100
cutoff=0.5
b,a=signal.butter(4,cutoff,fs=fs,btype='lowpass')
smoothened_data=signal.filtfilt(b,a,total_noise)


hours_average=[np.mean(i) for i in range(0,len(smoothened_data),60)]
hours=np.arange(0,24)

print("vehicles passing each hour: ",hours_average)
def heavy_traffic(vehicle_count,hours_average):
    for count in vehicle_count:
        for hours in hours_average:
            if count > 120 and hours>15:
                plt.plot(hours,count)
                
            
        
    
heavy_traffic(vehicle_count,hours_average)    
plt.subplot(1,3,1)
plt.ylim(0,10)
plt.plot(vehicle_count,total_noise)

plt.subplot(1,3,2)
plt.ylim(0,10)
plt.plot(vehicle_count,smoothened_data)

plt.subplot(1,3,3)
plt.ylim(0,60)
plt.plot(vehicle_count,hours_average,marker='o')
plt.show()




