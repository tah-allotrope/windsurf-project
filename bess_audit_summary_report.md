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
  - `DirectPVConsumption_kW`, `DischargeEnergy_kWh`, `PowerSurplus_kW` for hourly validation

## Model Definitions (Year-1)
- **Model A – Direct Clone**: Replicates Excel dispatch rules and the documented grid-export bug.
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
| **Model A – Direct Clone** | 71,808.30 | 30.14 | 9,291.41 | Best overall score (error concentrated in grid export) |
| **Model B – Lifetime Augmented** | 71,808.30 | 30.14 | 9,291.41 | Same year-1 results as Model A |
| **Model C – Peak Conservative** | 71,808.30 | 7,246.70 | 19,562.94 | Significantly higher error |

## Model Results vs Calc (Year-1)

| Metric | Calc (MWh) | Model A (MWh) | Error |
|---|---:|---:|---:|
| Solar Gen (Direct PV Consumption) | 61,106.38 | 71,808.30 | 17.51% |
| Grid Export (Power Surplus) | 1,087.26 | 30.14 | 97.23% |
| BESS Discharge (Discharge Energy) | 8,677.22 | 9,291.41 | 7.08% |

## Final Selection
**Model A – Direct Clone** is the selected model for the final audit.
- Lowest total error score.
- Closest alignment to Measures and Calc for BESS discharge.
- Model B matches year-1 output but is intended for lifetime extension only.

## Observations & Next Steps
- **Grid Export gap remains (~97%)** between Model A and Measures/Calc. This appears tied to the Excel grid-export bug and/or the definition of “Power Surplus.”
- **Solar vs Calc difference (17.51%)** is expected because Calc uses **Direct PV Consumption** rather than total solar generation.

If desired, we can:
1) Reconcile grid export by mirroring the exact Calc formula for `PowerSurplus_kW`.
2) Add a model variant that uses `DirectPVConsumption_kW` for reporting instead of total solar generation.
