"""Create a short animation showing how the seasonal curves build up."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

from wind_model import RATED_POWER_KW, available_wind_power_kw

WIND_SPEEDS = np.linspace(0, 15, 151)
SUMMER = available_wind_power_kw(WIND_SPEEDS, 1.12, 0.97)
WINTER = available_wind_power_kw(WIND_SPEEDS, 1.21, 0.97)

SUMMER_COLOR = "#8ea6bf"
WINTER_COLOR = "#5f7f9d"
RATED_COLOR = "#adb9c4"
TEXT_COLOR = "#33404d"


def main() -> None:
    Path("images").mkdir(exist_ok=True)
    figure, axis = plt.subplots(figsize=(8.2, 4.9))
    summer_line, = axis.plot([], [], linewidth=2.4, color=SUMMER_COLOR, label="Summer")
    winter_line, = axis.plot([], [], linewidth=2.4, color=WINTER_COLOR, label="Winter")
    axis.axhline(RATED_POWER_KW, linestyle=":", linewidth=1.3, color=RATED_COLOR, label="Rated power")
    axis.set_title("Seasonal Power-Curve Simulation", fontsize=13.5, fontweight="bold", color=TEXT_COLOR, pad=10)
    axis.set_xlabel("Wind speed (m/s)", fontsize=11.5, fontweight="bold", color=TEXT_COLOR)
    axis.set_ylabel("Power output (kW)", fontsize=11.5, fontweight="bold", color=TEXT_COLOR)
    axis.set_xlim(0, 15)
    axis.set_ylim(0, 6120)
    axis.tick_params(labelsize=9.5, colors=TEXT_COLOR)
    axis.grid(True, linestyle="--", alpha=0.18, color="#b8c2cc")
    axis.legend(loc="lower right", frameon=False, fontsize=9.6)

    def update(frame: int):
        end = max(2, frame)
        summer_line.set_data(WIND_SPEEDS[:end], SUMMER[:end])
        winter_line.set_data(WIND_SPEEDS[:end], WINTER[:end])
        return summer_line, winter_line

    animation = FuncAnimation(
        figure,
        update,
        frames=range(2, len(WIND_SPEEDS) + 1, 4),
        interval=70,
        blit=True,
    )
    animation.save(
        "images/wind_turbine_demo.gif",
        writer=PillowWriter(fps=12),
        dpi=100,
    )
    plt.close(figure)


if __name__ == "__main__":
    main()
