import unittest
import numpy as np
import pandas as pd
from excel_replica.model.financial import FinancialConfig, run_financial_model

class TestFinancialModel(unittest.TestCase):
    def setUp(self):
        self.cfg = FinancialConfig(
            land_cost_usd=1000000,
            pv_cost_usd=5000000,
            bess_cost_usd=4000000,
            leverage_ratio=0.5,
            interest_rate=0.08,
            debt_tenor_years=10,
            project_years=25
        )
        # 25 years of constant generation
        self.lifetime_results = pd.DataFrame({
            "SolarGen_MWh": [10000] * 25
        })
        self.revenue_per_mwh = 50.0

    def test_run_financial_model_basic(self):
        results = run_financial_model(
            self.lifetime_results,
            self.revenue_per_mwh,
            self.cfg
        )

        self.assertGreater(results.project_irr, -1.0)
        self.assertGreater(results.equity_irr, -1.0)
        self.assertEqual(len(results.yearly), 25)

        # Total CAPEX = 1 + 5 + 4 = 10M
        # Equity = 5M, Debt = 5M
        # Year 1 Revenue = 10000 * 50 = 500k
        self.assertAlmostEqual(results.yearly.iloc[0]["Revenue_USD"], 500000.0)

if __name__ == "__main__":
    unittest.main()
