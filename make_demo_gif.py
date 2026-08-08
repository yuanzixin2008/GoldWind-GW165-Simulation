"""Create a short animation showing how the seasonal curves build up."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

from wind_model import RATED_POWER_KW, available_wind_power_kw

WIND_SPEEDS = np.linspace(0, 25, 251)
SUMMER = available_wind_power_kw(WIND_SPEEDS, 1.12, 0.97)
WINTER = available_wind_power_kw(WIND_SPEEDS, 1.21, 0.97)


def main() -> None:
    Path("images").mkdir(exist_ok=True)
    figure, axis = plt.subplots(figsize=(8, 4.8))
    summer_line, = axis.plot([], [], linewidth=2, label="Summer")
    winter_line, = axis.plot([], [], linewidth=2, label="Winter")
    axis.axhline(RATED_POWER_KW, linestyle=":", linewidth=1.2, label="Rated power")
    axis.set(title="Seasonal Power-Curve Simulation", xlabel="Wind speed (m/s)", ylabel="Power output (kW)")
    axis.set_xlim(0, 25)
    axis.set_ylim(0, 6500)
    axis.grid(True, linestyle="--", alpha=0.3)
    axis.legend(loc="lower right")

    def update(frame: int):
        end = max(2, frame)
        summer_line.set_data(WIND_SPEEDS[:end], SUMMER[:end])
        winter_line.set_data(WIND_SPEEDS[:end], WINTER[:end])
        return summer_line, winter_line

    animation = FuncAnimation(figure, update, frames=range(2, len(WIND_SPEEDS), 5), interval=70, blit=True)
    animation.save("images/wind_turbine_demo.gif", writer=PillowWriter(fps=12), dpi=100)
    plt.close(figure)


if __name__ == "__main__":
    main()
