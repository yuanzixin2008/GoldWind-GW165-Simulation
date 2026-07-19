import matplotlib.pyplot as plt
import numpy as np

wind_speed=10
blade_length=81
rotor_area=np.pi*(blade_length**2)
power_coefficient=0.45
power_maximum=6000

sites=['Aksu2','Beyyurdu','Menekse','Soke','Sule','Usak','Mutlu','Cerkes']
densities=np.array([1.02,1.04,1.035,1.134,0.972,1.034,1.046,1.148])


wind_power=0.5*densities*rotor_area*(wind_speed**3)*power_coefficient
PMDD_eff=1
PMDD_generator_eff=0.97
PMDD_total=PMDD_eff*PMDD_generator_eff
raw_power=wind_power*PMDD_total/1000
real_power=np.clip(raw_power,0,power_maximum)


plt.figure(figsize=(11,6),dpi=100)
plt.grid(True,axis='y',linestyle='--',alpha=0.3)
bars=plt.bar(sites,real_power,color='#91EB9C',edgecolor='#4A4A4A',width=0.5,alpha=1)
for bar in bars:
    height=bar.get_height()
    plt.text(bar.get_x()+(bar.get_width()/2.0),height+100, f'{int(height)} kW',ha='center',va='bottom',color='#2C3E50',fontsize=8.5,fontweight='bold')
plt.xlabel('Turkey Sites',labelpad=10,fontsize=14)
plt.ylabel('Power Output (kW)',labelpad=10,fontsize=14)
plt.title('Turkey Wind Farms Power Output',fontsize=16,fontweight='bold')
plt.ylim(4000, 6000)
plt.tight_layout()
plt.show()


