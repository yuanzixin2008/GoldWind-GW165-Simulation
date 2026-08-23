import numpy as np
import matplotlib.pyplot as plt

wind_speed = 10
blade_length = 81
rotor_area = np.pi * blade_length**2
power_coefficient = 0.45
rated_power = 6000
pmdd_efficiency = 1.00 * 0.97

sites = [
    "Aksu2", "Beyyurdu", "Menekse", "Soke",
    "Sule", "Usak", "Mutlu", "Cerkes"
]
air_density = np.array([
    1.020, 1.040, 1.035, 1.134,
    0.972, 1.034, 1.046, 1.148
])

wind_power = (
    0.5 * air_density * rotor_area * wind_speed**3 * power_coefficient
)
power = np.clip(wind_power * pmdd_efficiency / 1000, 0, rated_power)

plt.figure(figsize=(11, 6.4), dpi=160)
bars = plt.bar(sites, power, width=0.62, edgecolor="0.3")
plt.grid(True, axis="y", linestyle="--", alpha=0.35)

for bar, value in zip(bars, power):
    x = bar.get_x() + bar.get_width() / 2
    plt.text(
        x, value + 90, f"{value:,.0f} kW",
        ha="center", va="bottom", fontsize=9.3, fontweight="bold"
    )

plt.title("Turkey Wind Farms", fontsize=16, weight="bold")
plt.xlabel("Site", fontsize=12)
plt.ylabel("Power output at 10 m/s (kW)", fontsize=12)
plt.ylim(0, 6000)
plt.tight_layout()
plt.savefig("Turkey_Wind_Farms.png", bbox_inches="tight")
plt.close()
