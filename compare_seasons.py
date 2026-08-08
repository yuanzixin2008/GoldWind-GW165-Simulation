"""Compare simplified summer and winter power curves."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from wind_model import RATED_POWER_KW, available_wind_power_kw, first_rated_speed

WIND_SPEEDS = np.linspace(0, 15, 151)
PMDD_EFFICIENCY = 0.97
SUMMER_DENSITY = 1.12
WINTER_DENSITY = 1.21

SUMMER_COLOR = "#8ea6bf"
WINTER_COLOR = "#5f7f9d"
FILL_COLOR = "#dbe4ec"
RATED_COLOR = "#adb9c4"
TEXT_COLOR = "#33404d"


def main() -> None:
    Path("images").mkdir(exist_ok=True)

    summer_power = available_wind_power_kw(WIND_SPEEDS, SUMMER_DENSITY, PMDD_EFFICIENCY)
    winter_power = available_wind_power_kw(WIND_SPEEDS, WINTER_DENSITY, PMDD_EFFICIENCY)

    summer_rated = first_rated_speed(WIND_SPEEDS, summer_power)
    winter_rated = first_rated_speed(WIND_SPEEDS, winter_power)

    plt.figure(figsize=(10.2, 6.2))
    plt.plot(
        WIND_SPEEDS,
        summer_power,
        label=f"Summer density: {SUMMER_DENSITY} kg/m³",
        linewidth=2.5,
        color=SUMMER_COLOR,
    )
    plt.plot(
        WIND_SPEEDS,
        winter_power,
        label=f"Winter density: {WINTER_DENSITY} kg/m³",
        linewidth=2.5,
        color=WINTER_COLOR,
    )
    plt.fill_between(
        WIND_SPEEDS,
        summer_power,
        winter_power,
        alpha=0.35,
        color=FILL_COLOR,
        label="Seasonal difference",
    )
    plt.axhline(
        RATED_POWER_KW,
        linestyle=":",
        linewidth=1.5,
        color=RATED_COLOR,
        label="Rated power: 6,000 kW",
    )

    if winter_rated is not None:
        plt.scatter([winter_rated], [RATED_POWER_KW], s=38, zorder=4, color=WINTER_COLOR)
        plt.annotate(
            f"Winter reaches rated output\nat about {winter_rated:.1f} m/s",
            xy=(winter_rated, RATED_POWER_KW),
            xytext=(7.2, 5650),
            arrowprops={"arrowstyle": "->", "linewidth": 0.9, "color": WINTER_COLOR},
            fontsize=9.2,
            color=TEXT_COLOR,
        )
    if summer_rated is not None:
        plt.scatter([summer_rated], [RATED_POWER_KW], s=38, zorder=4, color=SUMMER_COLOR)
        plt.annotate(
            f"Summer reaches rated output\nat about {summer_rated:.1f} m/s",
            xy=(summer_rated, RATED_POWER_KW),
            xytext=(10.0, 5250),
            arrowprops={"arrowstyle": "->", "linewidth": 0.9, "color": SUMMER_COLOR},
            fontsize=9.2,
            color=TEXT_COLOR,
        )

    plt.title("Effect of Seasonal Air Density on Modelled Power", fontsize=15, fontweight="bold", color=TEXT_COLOR, pad=12)
    plt.xlabel("Wind speed (m/s)", fontsize=12.5, fontweight="bold", color=TEXT_COLOR)
    plt.ylabel("Electrical power output (kW)", fontsize=12.5, fontweight="bold", color=TEXT_COLOR)
    plt.xlim(0, 15)
    plt.ylim(0, 6120)
    plt.xticks(fontsize=10.5, color=TEXT_COLOR)
    plt.yticks(fontsize=10.5, color=TEXT_COLOR)
    plt.grid(True, linestyle="--", alpha=0.20, color="#b8c2cc")
    plt.legend(loc="lower right", frameon=False, fontsize=10.0)
    plt.tight_layout()
    plt.savefig("images/seasonal_comparison.png", dpi=220)
    plt.close()

    print(f"Summer reaches rated power at about {summer_rated:.1f} m/s")
    print(f"Winter reaches rated power at about {winter_rated:.1f} m/s")


if __name__ == "__main__":
    main()
