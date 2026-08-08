"""Compare site scenarios using the air-density values in this project."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from wind_model import available_wind_power_kw

WIND_SPEED_MS = 10.0
PMDD_EFFICIENCY = 0.97

SITES = ["Aksu2", "Beyyurdu", "Menekse", "Soke", "Sule", "Usak", "Mutlu", "Cerkes"]
AIR_DENSITIES = np.array([1.020, 1.040, 1.035, 1.134, 0.972, 1.034, 1.046, 1.148])

BAR_COLOR = "#90a8bf"
EDGE_COLOR = "#758ea5"
TEXT_COLOR = "#33404d"


def main() -> None:
    Path("images").mkdir(exist_ok=True)

    outputs = np.array(
        [available_wind_power_kw(WIND_SPEED_MS, density, PMDD_EFFICIENCY).item()
         for density in AIR_DENSITIES]
    )

    order = np.argsort(outputs)
    sorted_sites = [SITES[index] for index in order]
    sorted_outputs = outputs[order]

    x = np.arange(len(sorted_sites))
    plt.figure(figsize=(10.2, 6.4))
    bars = plt.bar(x, sorted_outputs, width=0.62, color=BAR_COLOR, edgecolor=EDGE_COLOR, linewidth=0.8)
    plt.grid(True, axis="y", linestyle="--", alpha=0.18, color="#b8c2cc")
    plt.title(f"Site Scenario Comparison at {WIND_SPEED_MS:.0f} m/s", fontsize=15, fontweight="bold", color=TEXT_COLOR, pad=12)
    plt.xlabel("Site", fontsize=12.5, fontweight="bold", color=TEXT_COLOR)
    plt.ylabel("Modelled electrical power output (kW)", fontsize=12.5, fontweight="bold", color=TEXT_COLOR)
    plt.xticks(x, sorted_sites, fontsize=10.5, color=TEXT_COLOR)
    plt.yticks(fontsize=10.5, color=TEXT_COLOR)
    plt.ylim(0, sorted_outputs.max() + 550)
    plt.xlim(-0.6, len(sorted_sites)-0.4)

    for bar, output in zip(bars, sorted_outputs):
        plt.text(bar.get_x() + bar.get_width() / 2, output + 40, f"{output:.0f}", ha="center", va="bottom", fontsize=9.2, color=TEXT_COLOR)

    plt.tight_layout()
    plt.savefig("images/site_comparison.png", dpi=220)
    plt.close()

    best_index = int(np.argmax(outputs))
    print(f"Highest modelled output: {SITES[best_index]} ({outputs[best_index]:.0f} kW)")


if __name__ == "__main__":
    main()
