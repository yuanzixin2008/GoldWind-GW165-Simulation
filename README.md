# Wind Turbine Performance & Efficiency Simulation
> Based on the technical specifications of Goldwind **GW165-6.0** wind turbine.

## 📌Project Overview
This project establishes a mathematical and aerodynamic simulation framework to evaluate the power generation performance of modern wind turbines under various technical and environmental conditions.

## 🔧Simulation Phases

### Phase 1  📂 [Explore Phase 1 Branch & Source Code](../../tree/Phase1)
* **Focus**: Compare Permanent Magnet Direct-Drive (PMDD) system against traditional gear-driven turbines.
* **Core Logic**: $P = \frac{1}{2} \cdot \rho \cdot A \cdot v^3 \cdot C_p \cdot \eta_{total}$
* **Result**: PMDD system (without gearbox) improves the overall efficiency to 97%, eliminating mechanical wear and capturing more wind energy at mid-range wind speeds.

### Phase 2  📂 [Explore Phase 2 Branch & Source Code](../../tree/Phase2)
* **Focus**: The critical impact of seasonal air density changes ($\rho_{summer}=1.12$ , $\rho_{winter}=1.21$).
* **Result**: Quantified the "Seasonal Gap" indicating that dense winter air allows the turbine to reach its 6000 kW rated capacity at a lower rated wind speed (10.39 m/s) compared to summer (10.64 m/s).

### Phase 3 : Spatial Analysis(Turkey Wind Farm Sites)  📂 [Explore Phase 3 Branch & Source Code](../../tree/Phase3)
* **Focus**: Micro-siting resource evaluation across 8 different regions in Turkey at a constant wind speed of 10 m/s.
* **Visual Optimization**: Cropped the axis to `[4000, 6000]` kW to explicitly highlight spatial variations caused purely by local elevation and air density differences.


  | Site Name | Air Density ($\text{kg/m}^3$) | Elevation (m) | Turbulence Intensity (%) |
  | :--- | :---: | :---: | :---: |
  | **Aksu2** | 1.020 | 1630 | 8% |
  | **Beyyurdu**| 1.040 | 1550 | 8% |
  | **Menekse** | 1.035 | 1400 | 6% |
  | **Soke** | 1.134 | 540 | N/A |
  | **Sule** | 0.972 | 2200 | 8% |
  | **Usak** | 1.034 | 1350 | N/A |
  | **Mutlu** | 1.046 | 1205 | 6% |
  | **Cerkes** | 1.148 | 1900 | 14.40% |
