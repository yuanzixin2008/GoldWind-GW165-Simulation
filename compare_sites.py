"""Compare site scenarios using the air-density values in this project."""

import matplotlib.pyplot as plt
import numpy as np

from wind_model import available_wind_power_kw

WIND_SPEED_MS = 10.0
PMDD_EFFICIENCY = 0.97

SITES = ["Aksu2", "Beyyurdu", "Menekse", "Soke", "Sule", "Usak", "Mutlu", "Cerkes"]
AIR_DENSITIES = np.array([1.020, 1.040, 1.035, 1.134, 0.972, 1.034, 1.046, 1.148])


def main() -> None:
    outputs = np.array(
        [available_wind_power_kw(WIND_SPEED_MS, density, PMDD_EFFICIENCY).item()
         for density in AIR_DENSITIES]
    )

    order = np.argsort(outputs)
    sorted_sites = [SITES[index] for index in order]
    sorted_outputs = outputs[order]

    plt.figure(figsize=(10, 6))
    bars = plt.barh(sorted_sites, sorted_outputs)
    plt.grid(True, axis="x", linestyle="--", alpha=0.3)
    plt.title(f"Site Scenario Comparison at {WIND_SPEED_MS:.0f} m/s")
    plt.xlabel("Modelled electrical power output (kW)")
    plt.ylabel("Site")
    plt.xlim(max(0, sorted_outputs.min() - 500), sorted_outputs.max() + 450)

    for bar, output in zip(bars, sorted_outputs):
        plt.text(output + 35, bar.get_y() + bar.get_height() / 2, f"{output:.0f} kW", va="center", fontsize=9)

    plt.tight_layout()
    plt.savefig("images/site_comparison.png", dpi=220)
    plt.close()

    best_index = int(np.argmax(outputs))
    print(f"Highest modelled output: {SITES[best_index]} ({outputs[best_index]:.0f} kW)")


if __name__ == "__main__":
    main()
