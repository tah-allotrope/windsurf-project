import unittest
import numpy as np
import pandas as pd
from excel_replica.model.calc_engine import CalcConfig, run_calc

class TestCalcEngine(unittest.TestCase):
    def setUp(self):
        self.cfg = CalcConfig(
            step_hours=1.0,
            bess_capacity_kwh=100.0,
            bess_power_kw=50.0,
            bess_efficiency=0.9,
            min_soc_kwh=0.0,
            ca_peak=1.0,
            ca_normal=0.5,
            ca_offpeak=0.1
        )
        self.hours = 24
        self.datetime_series = pd.date_range("2025-01-01", periods=self.hours, freq="h")
        self.solar_kw = np.zeros(self.hours)
        self.load_kw = np.zeros(self.hours)
        self.period_flags = np.array(["N"] * self.hours)
        self.allow_discharge = np.ones(self.hours, dtype=bool)

    def test_solar_only_consumption(self):
        # 100kW solar, 50kW load -> 50kW direct consumption, 50kW excess
        self.solar_kw[0] = 100.0
        self.load_kw[0] = 50.0

        # Disable charging to see surplus
        self.cfg.bess_capacity_kwh = 0.0

        results = run_calc(
            self.datetime_series, self.solar_kw, self.load_kw,
            self.period_flags, self.allow_discharge, self.cfg
        )

        self.assertEqual(results.hourly.iloc[0]["DirectPVConsumption_kW"], 50.0)
        self.assertEqual(results.hourly.iloc[0]["PowerSurplus_kW"], 50.0)
        self.assertEqual(results.outputs["solar_gen_mwh"], 0.1)

    def test_bess_charging(self):
        # 100kW solar, 0kW load -> all goes to BESS
        self.solar_kw[0] = 100.0
        self.load_kw[0] = 0.0

        results = run_calc(
            self.datetime_series, self.solar_kw, self.load_kw,
            self.period_flags, self.allow_discharge, self.cfg
        )

        # Charge is limited by power (50kW * 1h = 50kWh)
        self.assertEqual(results.hourly.iloc[0]["ChargeEnergy_kWh"], 50.0)
        # SOC after 1h should be 50kWh * 0.9 efficiency = 45kWh
        self.assertEqual(results.hourly.iloc[0]["SOC_kWh"], 45.0)

    def test_bess_discharging(self):
        # Hour 0: Charge BESS
        self.solar_kw[0] = 100.0
        self.load_kw[0] = 0.0

        # Hour 1: No solar, 50kW load -> Discharge BESS
        self.solar_kw[1] = 0.0
        self.load_kw[1] = 50.0

        results = run_calc(
            self.datetime_series, self.solar_kw, self.load_kw,
            self.period_flags, self.allow_discharge, self.cfg
        )

        # SOC after Hour 0 is 45kWh
        # Available discharge is 45kWh * 0.9 = 40.5kWh
        self.assertEqual(results.hourly.iloc[1]["DischargeEnergy_kWh"], 40.5)
        self.assertEqual(results.hourly.iloc[1]["GridLoad_kW"], 50.0 - 40.5)

if __name__ == "__main__":
    unittest.main()
