"""Compare simplified summer and winter power curves."""

import matplotlib.pyplot as plt
import numpy as np

from wind_model import RATED_POWER_KW, available_wind_power_kw, first_rated_speed

WIND_SPEEDS = np.linspace(0, 25, 251)
PMDD_EFFICIENCY = 0.97
SUMMER_DENSITY = 1.12
WINTER_DENSITY = 1.21


def main() -> None:
    summer_power = available_wind_power_kw(WIND_SPEEDS, SUMMER_DENSITY, PMDD_EFFICIENCY)
    winter_power = available_wind_power_kw(WIND_SPEEDS, WINTER_DENSITY, PMDD_EFFICIENCY)

    summer_rated = first_rated_speed(WIND_SPEEDS, summer_power)
    winter_rated = first_rated_speed(WIND_SPEEDS, winter_power)

    plt.figure(figsize=(10, 6))
    plt.plot(WIND_SPEEDS, summer_power, label=f"Summer density: {SUMMER_DENSITY} kg/m³", linewidth=2)
    plt.plot(WIND_SPEEDS, winter_power, label=f"Winter density: {WINTER_DENSITY} kg/m³", linewidth=2)
    plt.fill_between(WIND_SPEEDS, summer_power, winter_power, alpha=0.2, label="Seasonal difference")
    plt.axhline(RATED_POWER_KW, linestyle=":", linewidth=1.5, label="Rated power: 6,000 kW")

    if summer_rated is not None:
        plt.axvline(summer_rated, linestyle="--", alpha=0.65)
        plt.text(summer_rated + 0.2, 250, f"{summer_rated:.1f} m/s", rotation=90, va="bottom")
    if winter_rated is not None:
        plt.axvline(winter_rated, linestyle="--", alpha=0.65)
        plt.text(winter_rated - 0.5, 250, f"{winter_rated:.1f} m/s", rotation=90, va="bottom")

    plt.title("Effect of Seasonal Air Density on Modelled Power")
    plt.xlabel("Wind speed (m/s)")
    plt.ylabel("Electrical power output (kW)")
    plt.xlim(0, 25)
    plt.ylim(0, 6500)
    plt.grid(True, linestyle="--", alpha=0.35)
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig("images/seasonal_comparison.png", dpi=220)
    plt.close()

    print(f"Summer reaches rated power at about {summer_rated:.1f} m/s")
    print(f"Winter reaches rated power at about {winter_rated:.1f} m/s")


if __name__ == "__main__":
    main()
