# System Patterns (The Map)

## Architecture
SystemConfig (Inputs) -> BESSSimulator (Physics) -> FinancialCalculator (Cash Flow/Tax/MRA) -> ReportGenerator

## Data Flow
Hourly physics model (kW/kWh) -> Annual aggregation (MWh) -> Financial model (USD/VND conversion) -> Reports & audit outputs
