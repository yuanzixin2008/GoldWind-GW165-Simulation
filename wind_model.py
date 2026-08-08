"""Shared calculations for the simplified GW165 wind-turbine simulations."""

from __future__ import annotations

import numpy as np

RATED_POWER_KW = 6000.0
ROTOR_DIAMETER_M = 165.0
ROTOR_RADIUS_M = ROTOR_DIAMETER_M / 2
ROTOR_AREA_M2 = np.pi * ROTOR_RADIUS_M**2
POWER_COEFFICIENT = 0.45
CUT_IN_SPEED_MS = 3.0
CUT_OUT_SPEED_MS = 24.0


def available_wind_power_kw(
    wind_speed_ms: np.ndarray | float,
    air_density_kg_m3: float,
    efficiency: float,
) -> np.ndarray:
    """Return simplified electrical power output in kW.

    The model uses P = 0.5 * rho * A * v^3 * Cp * efficiency, then limits
    output to the turbine's rated power and applies cut-in/cut-out speeds.
    It is intended for comparison and learning, not engineering prediction.
    """
    speed = np.asarray(wind_speed_ms, dtype=float)
    raw_power_kw = (
        0.5
        * air_density_kg_m3
        * ROTOR_AREA_M2
        * speed**3
        * POWER_COEFFICIENT
        * efficiency
        / 1000
    )

    operating = (speed >= CUT_IN_SPEED_MS) & (speed <= CUT_OUT_SPEED_MS)
    return np.where(operating, np.clip(raw_power_kw, 0, RATED_POWER_KW), 0.0)


def first_rated_speed(wind_speed_ms: np.ndarray, power_kw: np.ndarray) -> float | None:
    """Return the first sampled wind speed that reaches rated power."""
    indices = np.flatnonzero(power_kw >= RATED_POWER_KW)
    if len(indices) == 0:
        return None
    return float(wind_speed_ms[indices[0]])
