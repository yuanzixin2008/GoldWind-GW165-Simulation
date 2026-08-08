"""Compare two simplified drivetrain-efficiency scenarios."""

import matplotlib.pyplot as plt
import numpy as np

from wind_model import RATED_POWER_KW, available_wind_power_kw

AIR_DENSITY = 1.225
WIND_SPEEDS = np.linspace(0, 25, 251)

# The PMDD value is based on technical material reviewed during my internship.
# The geared values are component-efficiency inputs used for comparison.
TRADITIONAL_EFFICIENCY = 0.94 * 0.95
PMDD_EFFICIENCY = 0.97


def main() -> None:
    traditional_power = available_wind_power_kw(
        WIND_SPEEDS, AIR_DENSITY, TRADITIONAL_EFFICIENCY
    )
    pmdd_power = available_wind_power_kw(WIND_SPEEDS, AIR_DENSITY, PMDD_EFFICIENCY)

    plt.figure(figsize=(10, 6))
    plt.plot(WIND_SPEEDS, traditional_power, label="Traditional geared drivetrain", linewidth=2)
    plt.plot(WIND_SPEEDS, pmdd_power, label="Goldwind PMDD drivetrain", linewidth=2)
    plt.axhline(RATED_POWER_KW, linestyle=":", linewidth=1.5, label="Rated power: 6,000 kW")
    plt.title("Simplified Drivetrain Efficiency Comparison")
    plt.xlabel("Wind speed (m/s)")
    plt.ylabel("Electrical power output (kW)")
    plt.xlim(0, 25)
    plt.ylim(0, 6500)
    plt.grid(True, linestyle="--", alpha=0.35)
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig("images/drivetrain_comparison.png", dpi=220)
    plt.close()

    difference = np.max(pmdd_power - traditional_power)
    print(f"Maximum modelled output difference: {difference:.1f} kW")


if __name__ == "__main__":
    main()
