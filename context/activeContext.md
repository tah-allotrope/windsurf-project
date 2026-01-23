# Active Context (The State)

## Current Focus
- Full model pipeline operational: Calc → Lifetime → Financial → DPPA

## Recent Changes
- **Regression suite PASS** (0.00% error on solar_gen, discharge, power_surplus)
- Loaded tariff rates from Assumption sheet (Ca_peak=0.0832, Ca_normal=0.0482, Ca_offpeak=0.0324 USD/kWh)
- Validated Financial model structure against Excel (CAPEX matches exactly: $49,513,200)
- Implemented `excel_replica/model/dppa.py` with:
  - FMP/CFMP pricing logic
  - CfD settlement calculation
  - Strike price and PCL handling

## Validated Parameters
- Usable capacity: 56,100 kWh (66,000 × 0.85 DoD)
- Power: 20,000 kW
- Efficiency: 0.95 (half-cycle)
- Min SOC threshold: 215 kWh
- Augmentation years: 11, 22
- Strike Price: 1,800 VND/kWh
- PCL: 163.2 VND/kWh
- Exchange Rate: 26,000 VND/USD

## Module Status
| Module | Status | File |
|--------|--------|------|
| Calc Engine | ✅ PASS | `excel_replica/model/calc_engine.py` |
| Lifetime | ✅ Done | `excel_replica/model/lifetime.py` |
| Financial | ✅ Done | `excel_replica/model/financial.py` |
| DPPA | ✅ Done | `excel_replica/model/dppa.py` |
| Regression | ✅ PASS | `excel_replica/validation/regression_suite.py` |

## Next Steps
- Fine-tune Financial model debt service to match Excel Equity IRR
- Add end-to-end pipeline runner combining all modules
- Generate audit report comparing Python vs Excel outputs
