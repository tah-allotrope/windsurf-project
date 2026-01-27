# Scenario Validation Harness

This harness lets you validate the Python model against Excel on synthetic inputs.

## How it works
1. Copy the base Excel workbook.
2. Apply per-scenario overrides to the copy.
3. Recalculate in Excel (COM automation if available).
4. Run the audit report against the modified workbook.

## Scenario JSON format
```json
{
  "name": "scenario_name",
  "description": "What this scenario represents",
  "overrides": [
    {"sheet": "Assumption", "cell": "K18", "value": 30.0}
  ]
}
```

## Usage
```bash
python -m excel_replica.validation.scenario_runner \
  --base-excel "AUDIT 20251201 40MW Solar ^M BESS Ecoplexus.xlsx" \
  --scenarios-dir "excel_replica/validation/scenarios" \
  --output-dir "excel_replica/validation/outputs"
```

## Recalculation note
If COM automation is unavailable or fails, open each scenario Excel file once in Excel, let it recalc, save, then rerun the scenario runner.

## Included examples
- `scenario_small_scale.json`: reduced solar + BESS scale
- `scenario_high_opex.json`: higher O&M + insurance
