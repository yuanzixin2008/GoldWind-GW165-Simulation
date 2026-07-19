import matplotlib.pyplot as plt
import numpy as np
#====================================
#Constant and Simulated Parameters

air_density=1.225
power_coefficient=0.45
blade_length=81
power_maximum=6000
#Rotor Swept Area=π*r^2
rotor_area=np.pi*(blade_length**2)
wind_speed=np.linspace(3,15,100)
#========================================
#Difference of Wind Turbin Efficiency

#Traditional Wind Turbine(with gearbox)
gearbox_eff=0.94
generator_eff=0.95
traditional_total=gearbox_eff*generator_eff

#Goldwind PMDD Turbine(without gearbox)
PMDD_eff=1
PMDD_generator_eff=0.97
PMDD_total=PMDD_eff*PMDD_generator_eff
#============================================
#Power Calculation Formula(P=0.5*ρ*A*v^3*Cp*η)
wind_power=0.5*air_density*rotor_area*(wind_speed**3)*power_coefficient

raw_traditional_power=wind_power*traditional_total/1000
raw_PMDD_power=wind_power*PMDD_total/1000
traditional_power=np.clip(raw_traditional_power,0,power_maximum)
PMDD_power=np.clip(raw_PMDD_power,0,power_maximum)

#==============================================
#Plot a Figure
plt.figure(figsize=(11,6),dpi=100)
plt.plot(wind_speed,traditional_power,label='Traditional Wind Turbine(with gearbox)',color='red',linewidth=2)
plt.plot(wind_speed,PMDD_power,label='Goldwind PMDD Turbine',color='green',linewidth=2)
plt.grid(True,linestyle='--',alpha=0.5)
plt.axhline(y=power_maximum,color='blue',linestyle=':',linewidth=1.5,alpha=0.6)
plt.text(3.8,power_maximum+50,'Goldwind GW165-6.0 Rated Capacity: 6000 kW',color='blue', fontsize=11, style='italic')
plt.title('Traditional Turbine vs Goldwind PMDD',fontsize=16,fontweight='bold')
plt.xlabel('Wind speed(m/s)',fontsize=14)
plt.ylabel('Power Output(kW)',fontsize=14)
plt.legend(loc='lower right',fontsize=12)
plt.xlim(3, 15)
plt.ylim(0, 6500)

plt.show()





