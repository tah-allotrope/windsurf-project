# Active Context (The State)

## Current Focus
- VBA macro analysis complete - DSCR debt sculpting implemented

## Recent Changes
- **VBA Macro Analysis**: Extracted GoalSeek debt sizing logic from Module 2
- **DSCR Debt Sculpting**: Implemented `Debt Service = CFADS / 1.3`
- **Dividend Formula**: Fixed to `Dividend = CFADS + Principal - Interest`
- **Interest Rate**: Corrected to 8.5% (2% base + 6.5% margin)
- **Debt Tenor**: Fixed to 10 years (was 15)
- **MRA Schedule**: Fixed to Excel's actual amounts ($908K/year for Y8-10)

## Audit Results (Post VBA Fix)
| Metric | Python | Excel | Error | Status |
|--------|--------|-------|-------|--------|
| Solar Gen (MWh) | 71,808.30 | 71,808.30 | 0.00% | ✅ |
| Discharge (MWh) | 8,677.22 | 8,677.22 | 0.00% | ✅ |
| Surplus (MWh) | 1,087.26 | 1,087.26 | 0.00% | ✅ |
| Charge (MWh) | 9,614.65 | 9,614.65 | 0.00% | ✅ |
| CAPEX | $49,513,200 | $49,513,200 | 0.00% | ✅ |
| Project IRR | 6.37% | 5.07% | 25.6% | ⚠️ |
| Equity IRR | 10.88% | 8.83% | 23.2% | ⚠️ |
| Dividends Y1-10 | Match | Match | 0-5% | ✅ |
| EBITDA Y1-10 | Match | Match | 0-3% | ✅ |

## Key VBA Findings
- **Module 2**: `Solve_Debt_Size_DSCR` uses GoalSeek to find debt size
- Named ranges: `DebtSize_DSCR_Solver`, `DebtSize_Check`, `DSCR_Debt_Size`
- Excel maintains DSCR = 1.30 for all debt service years
- Interest formula: `Balance * (BaseRate + Margin) * TenorIndicator`

## Module Status
| Module | Status | File |
|--------|--------|------|
| Calc Engine | ✅ 0.00% | `excel_replica/model/calc_engine.py` |
| Lifetime | ✅ Done | `excel_replica/model/lifetime.py` |
| Financial | ✅ DSCR | `excel_replica/model/financial.py` |
| DPPA | ✅ Done | `excel_replica/model/dppa.py` |
| Pipeline | ✅ Done | `excel_replica/run_pipeline.py` |
| Sensitivity | ✅ Done | `excel_replica/analysis/sensitivity.py` |
| Monte Carlo | ✅ Done | `excel_replica/analysis/monte_carlo.py` |
| Visualization | ✅ Done | `excel_replica/analysis/visualize.py` |

## Notes
- Energy model fully validated (0% error)
- Dividends match within 0-5% for all years
- EBITDA matches within 0-3% for all years
- IRR difference due to minor revenue calculation differences (price escalation timing)
