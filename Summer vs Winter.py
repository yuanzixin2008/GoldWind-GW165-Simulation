import matplotlib.pyplot as plt
import numpy as np
#===========constant and simulated parameters===========
blade_length=81
rotor_area=np.pi*(blade_length**2)
power_coefficient=0.45
PMDD_eff=1.0*0.97
power_maximum=6000
wind_speed=np.linspace(3,15,100)

#================Different air density=============
#Summer(Hot&Humid)
density_summer=1.12
summer_original=0.5*density_summer*rotor_area*(wind_speed**3)*power_coefficient*PMDD_eff/1000
power_summer=np.clip(summer_original,0,power_maximum)
wind_summer=wind_speed[np.where(power_summer>=power_maximum)[0][0]]
#Winter(Cool&Dry)
density_winter=1.21
winter_original=0.5*density_winter*rotor_area*(wind_speed**3)*power_coefficient*PMDD_eff/1000
power_winter=np.clip(winter_original,0,power_maximum)
wind_winter=wind_speed[np.where(power_winter>=power_maximum)[0][0]]
#========Plot a figure=========
plt.figure(figsize=(11,6))
plt.plot(wind_speed,power_summer,label='Summer',linewidth=1,color='#DD4343')
plt.plot(wind_speed,power_winter,label='Winter',linewidth=1,color='#091599')
plt.axhline(y=power_maximum,color='blue',linestyle=':',linewidth=1.5,alpha=0.6)
plt.text(3.8,power_maximum+50,'Goldwind GW165-6.0 Rated Capacity: 6000 kW',color='blue', fontsize=11, style='italic')
plt.vlines(x=wind_summer,ymin=0,ymax=power_maximum,color='#DD4343',linestyle='--',alpha=0.8,linewidth=1)
plt.text(wind_summer+0.1,100,f'{wind_summer:.2f}m/s',ha='left',va='bottom',fontweight='bold',fontsize=10,color='#DD4343')
plt.vlines(x=wind_winter,ymin=0,ymax=power_maximum,color='#091599',linestyle='--',alpha=0.8,linewidth=1)
plt.text(wind_winter-0.1,100,f'{wind_winter:.2f}m/s',ha='right',va='bottom',fontweight='bold',fontsize=10,color='#091599')
plt.grid(True,linestyle='--',alpha=0.5)
plt.title('The Difference of Power Output between Summer and Winter',fontsize=16,fontweight='bold')
plt.xlabel('Wind Speed(m/s)',fontsize=14)
plt.ylabel('Power Output(kW)',fontsize=14)
plt.fill_between(wind_speed,power_summer,power_winter,label='Seasonal Gap',color='gray',alpha=0.5)
plt.legend(loc='lower right',fontsize=12)
plt.xlim(3, 15)
plt.ylim(0, 6500)
plt.show()
