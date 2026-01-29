# BESS Audit Summary Report

## Objective
Validate three BESS logic models (Direct Clone, Lifetime Augmented, Peak Conservative) against the Excel audit model and select the best-performing model for the final audit.

## Data Sources
- Excel file: `AUDIT 20251201 40MW Solar ^M BESS Ecoplexus.xlsx`
- Measures labels confirmed:
  - **Total Solar Generation**
  - **PV Surplus** (used as Grid Export)
  - **BESS-To-Load** (used as BESS Discharge)
- Calc sheet references:
  - `TimePeriodFlag` for TOU
  - `SolarGen_kW`, `DischargeEnergy_kWh`, `PowerSurplus_kW` for hourly validation

## Model Definitions (Year-1)
- **Model A – Direct Clone**: Replicates Excel dispatch rules and Calc sheet formulas.
- **Model B – Lifetime Augmented**: Model A + PV/BESS degradation and augmentations (years 11, 21) across 25 years.
- **Model C – Peak Conservative**: Simplified peak-only discharge strategy.

## Measures Truth (Year-1)
All values scaled to **MWh** (Measures sheet reported kWh).

| Metric | Measures (MWh) |
|---|---:|
| Solar Generation | 71,808.30 |
| PV Surplus / Grid Export | 1,087.26 |
| BESS Discharge (BESS-To-Load) | 8,677.22 |

## Model Results vs Measures (Year-1)

| Model | Solar Gen (MWh) | Grid Export (MWh) | BESS Discharge (MWh) | Notes |
|---|---:|---:|---:|---|
| **Model A – Direct Clone** | 71,808.30 | 1,087.26 | 8,677.22 | Exact match to Measures truth |
| **Model B – Lifetime Augmented** | 71,808.30 | 1,087.26 | 8,677.22 | Same year-1 results as Model A |
| **Model C – Peak Conservative** | 71,808.30 | 2,360.53 | 7,522.78 | More conservative discharge, higher export |

## Model Results vs Calc (Year-1)

| Metric | Calc (MWh) | Model A (MWh) | Error |
|---|---:|---:|---:|
| Solar Gen (SolarGen_kW) | 71,808.30 | 71,808.30 | 0.00% |
| Grid Export (Power Surplus) | 1,087.26 | 1,087.26 | 0.00% |
| BESS Discharge (Discharge Energy) | 8,677.22 | 8,677.22 | 0.00% |

## Final Selection
**Model A – Direct Clone** is the selected model for the final audit.
- Lowest total error score.
- Closest alignment to Measures and Calc for BESS discharge.
- Model B matches year-1 output but is intended for lifetime extension only.

## Observations & Next Steps
- Model A now matches Calc/Measures for Grid Export and BESS Discharge using the aligned Calc formulas.
- Calc solar truth now references `SolarGen_kW` to compare total generation consistently with Measures.

If desired, we can:
1) Reconcile grid export by mirroring the exact Calc formula for `PowerSurplus_kW`.
2) Add a model variant that uses `DirectPVConsumption_kW` for reporting instead of total solar generation.
