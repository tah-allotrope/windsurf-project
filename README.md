# Solar+BESS Techno-Economic Audit Model (Vietnam)

This project is a Python-based replication and audit tool for a legacy Excel model of a Solar + Battery Energy Storage System (BESS) project in Vietnam.

## Features
- **Hourly Calculation Engine**: Replicates Excel logic for solar generation, BESS dispatch, and TOU (Time-of-Use) pricing.
- **Lifetime Simulation**: Models 25-year project life including PV and BESS degradation, with battery augmentation in Years 11 and 22.
- **Financial Model**: Calculates Project IRR, Equity IRR, NPV, and Payback period. Includes Vietnam-specific tax holidays and debt sculpting logic.
- **DPPA Pricing**: Optional module for Direct Power Purchase Agreement settlement (FMP vs CfD).
- **Audit Tool**: Automatically compares Python outputs against Excel truth values and generates a Markdown report.

## Project Structure
- `excel_replica/`: Main package
  - `model/`: Core calculation modules (calc_engine, financial, lifetime, dppa)
  - `utils/`: Helpers (Excel reader using named ranges)
  - `outputs/`: Report generation
  - `config/`: Named range mappings and configuration
- `tests/`: Unit tests for core logic
- `legacy/`: Archive of older or standalone model scripts

## Installation

1. Ensure you have Python 3.8+ installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run Full Pipeline
To run the end-to-end simulation:
```bash
python -m excel_replica.run_pipeline
```

### Run Audit Report
To compare Python results with the Excel model:
```bash
python -m excel_replica.outputs.audit_report
```
The report will be saved to `excel_replica/outputs/audit_report.md`.

### Run Tests
```bash
python -m unittest discover tests
```

## Audit Status
Currently, the model matches the Excel truth values with high accuracy:
- Energy Metrics: 0.00% error
- Project IRR: < 10% error
- Equity IRR: < 5% error
- NPV: 0.00% error (when using Excel EBITDA inputs)
