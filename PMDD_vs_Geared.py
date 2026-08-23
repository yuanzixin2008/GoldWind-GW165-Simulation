import numpy as np
import matplotlib.pyplot as plt

air_density = 1.225
power_coefficient = 0.45
blade_length = 81
rated_power = 6000
rotor_area = np.pi * blade_length**2
wind_speed = np.linspace(3, 15, 200)

geared_efficiency = 0.94 * 0.95
pmdd_efficiency = 1.00 * 0.97

wind_power = 0.5 * air_density * rotor_area * wind_speed**3 * power_coefficient

geared_raw = wind_power * geared_efficiency / 1000
pmdd_raw = wind_power * pmdd_efficiency / 1000

geared_power = np.clip(geared_raw, 0, rated_power)
pmdd_power = np.clip(pmdd_raw, 0, rated_power)

compare_speed = 10
i = np.argmin(np.abs(wind_speed - compare_speed))
geared_10 = geared_power[i]
pmdd_10 = pmdd_power[i]
difference = pmdd_10 - geared_10
difference_pct = difference / geared_10 * 100

geared_rated = wind_speed[np.where(geared_power >= rated_power)[0][0]]
pmdd_rated = wind_speed[np.where(pmdd_power >= rated_power)[0][0]]

plt.figure(figsize=(11, 6.4), dpi=160)
plt.plot(wind_speed, geared_power, linewidth=2.5, label="Geared turbine")
plt.plot(wind_speed, pmdd_power, linewidth=2.5, label="PMDD turbine")
plt.axhline(rated_power, linestyle="--", linewidth=1.3, alpha=0.75)
plt.scatter([compare_speed, compare_speed], [geared_10, pmdd_10], s=36, zorder=5)

plt.text(3.1, 6125, "Rated capacity = 6000 kW", fontsize=10)

summary = (
    f"At 10 m/s\n"
    f"PMDD: {pmdd_10:,.0f} kW\n"
    f"Geared: {geared_10:,.0f} kW\n"
    f"Difference: +{difference:,.0f} kW ({difference_pct:.1f}%)\n\n"
    f"6000 kW reached at\n"
    f"PMDD: {pmdd_rated:.2f} m/s\n"
    f"Geared: {geared_rated:.2f} m/s"
)
plt.text(
    10.75, 2300, summary, fontsize=10.2,
    bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="0.7")
)

plt.title("PMDD vs Geared Turbine", fontsize=16, weight="bold")
plt.xlabel("Wind speed (m/s)", fontsize=12)
plt.ylabel("Power output (kW)", fontsize=12)
plt.xlim(3, 15)
plt.ylim(0, 6500)
plt.grid(True, linestyle="--", alpha=0.35)
plt.legend(loc="lower right")
plt.tight_layout()
plt.savefig("PMDD_vs_Geared.png", bbox_inches="tight")
plt.close()
