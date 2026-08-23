import numpy as np
import matplotlib.pyplot as plt

blade_length = 81
rotor_area = np.pi * blade_length**2
power_coefficient = 0.45
pmdd_efficiency = 1.00 * 0.97
rated_power = 6000
wind_speed = np.linspace(3, 15, 200)

summer_density = 1.12
winter_density = 1.21

summer_raw = (
    0.5 * summer_density * rotor_area * wind_speed**3
    * power_coefficient * pmdd_efficiency / 1000
)
winter_raw = (
    0.5 * winter_density * rotor_area * wind_speed**3
    * power_coefficient * pmdd_efficiency / 1000
)

summer_power = np.clip(summer_raw, 0, rated_power)
winter_power = np.clip(winter_raw, 0, rated_power)

compare_speed = 10
i = np.argmin(np.abs(wind_speed - compare_speed))
summer_10 = summer_power[i]
winter_10 = winter_power[i]
difference = winter_10 - summer_10
difference_pct = difference / summer_10 * 100

summer_rated = wind_speed[np.where(summer_power >= rated_power)[0][0]]
winter_rated = wind_speed[np.where(winter_power >= rated_power)[0][0]]

plt.figure(figsize=(11, 6.4), dpi=160)
plt.plot(wind_speed, summer_power, linewidth=2.5, label="Summer")
plt.plot(wind_speed, winter_power, linewidth=2.5, label="Winter")
plt.fill_between(wind_speed, summer_power, winter_power, alpha=0.16, label="Seasonal gap")
plt.axhline(rated_power, linestyle="--", linewidth=1.3, alpha=0.75)
plt.scatter([compare_speed, compare_speed], [summer_10, winter_10], s=36, zorder=5)

plt.text(3.1, 6125, "Rated capacity = 6000 kW", fontsize=10)

summary = (
    f"At 10 m/s\n"
    f"Winter: {winter_10:,.0f} kW\n"
    f"Summer: {summer_10:,.0f} kW\n"
    f"Difference: +{difference:,.0f} kW ({difference_pct:.1f}%)\n\n"
    f"6000 kW reached at\n"
    f"Winter: {winter_rated:.2f} m/s\n"
    f"Summer: {summer_rated:.2f} m/s"
)
plt.text(
    10.85, 2300, summary, fontsize=10.2,
    bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="0.7")
)

plt.title("Summer vs Winter", fontsize=16, weight="bold")
plt.xlabel("Wind speed (m/s)", fontsize=12)
plt.ylabel("Power output (kW)", fontsize=12)
plt.xlim(3, 15)
plt.ylim(0, 6500)
plt.grid(True, linestyle="--", alpha=0.35)
plt.legend(loc="lower right")
plt.tight_layout()
plt.savefig("Summer_vs_Winter.png", bbox_inches="tight")
plt.close()
