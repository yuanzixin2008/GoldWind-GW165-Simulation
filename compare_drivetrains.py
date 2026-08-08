"""Compare two simplified drivetrain-efficiency scenarios."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from wind_model import RATED_POWER_KW, available_wind_power_kw

AIR_DENSITY = 1.225
WIND_SPEEDS = np.linspace(0, 15, 151)

TRADITIONAL_EFFICIENCY = 0.94 * 0.95
PMDD_EFFICIENCY = 0.97

TRADITIONAL_COLOR = "#7f93a6"
PMDD_COLOR = "#5e7c99"
RATED_COLOR = "#aab7c4"
TEXT_COLOR = "#33404d"


def main() -> None:
    Path("images").mkdir(exist_ok=True)

    traditional_power = available_wind_power_kw(
        WIND_SPEEDS, AIR_DENSITY, TRADITIONAL_EFFICIENCY
    )
    pmdd_power = available_wind_power_kw(WIND_SPEEDS, AIR_DENSITY, PMDD_EFFICIENCY)

    plt.figure(figsize=(10.2, 6.2))
    plt.plot(
        WIND_SPEEDS,
        traditional_power,
        label="Traditional geared drivetrain",
        linewidth=2.6,
        color=TRADITIONAL_COLOR,
    )
    plt.plot(
        WIND_SPEEDS,
        pmdd_power,
        label="Goldwind PMDD drivetrain",
        linewidth=2.6,
        color=PMDD_COLOR,
    )
    plt.axhline(
        RATED_POWER_KW,
        linestyle=":",
        linewidth=1.6,
        color=RATED_COLOR,
        label="Rated power: 6,000 kW",
    )
    plt.title(
        "Simplified Drivetrain Efficiency Comparison",
        fontsize=15,
        fontweight="bold",
        color=TEXT_COLOR,
        pad=12,
    )
    plt.xlabel("Wind speed (m/s)", fontsize=12.5, fontweight="bold", color=TEXT_COLOR)
    plt.ylabel("Electrical power output (kW)", fontsize=12.5, fontweight="bold", color=TEXT_COLOR)
    plt.xlim(0, 15)
    plt.ylim(0, 6200)
    plt.xticks(fontsize=10.5, color=TEXT_COLOR)
    plt.yticks(fontsize=10.5, color=TEXT_COLOR)
    plt.grid(True, linestyle="--", alpha=0.20, color="#b8c2cc")
    plt.legend(loc="lower right", frameon=False, fontsize=10.2)
    plt.tight_layout()
    plt.savefig("images/drivetrain_comparison.png", dpi=220)
    plt.close()

    difference = np.max(pmdd_power - traditional_power)
    print(f"Maximum modelled output difference: {difference:.1f} kW")


if __name__ == "__main__":
    main()
