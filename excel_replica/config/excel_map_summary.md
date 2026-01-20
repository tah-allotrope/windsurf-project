# Excel Formula Map Summary (Deep Scan)

Source: `excel_replica/config/excel_map.json`

## DPPA Sheet Formula Patterns (Top 12)
- **7,762** × `IF(Does_model_is_actived?, LET(XLOOKUP(... SimulationData[DateTime] ... CHOOSECOLS(... {4,5,6}), {0,0,0}))`
- **7,762** × `XLOOKUP($A#, Calc!$A$#:$A$####, Calc!$E$#:$E$####, 0, 0, 2)`
- **7,762** × `IF(Does_model_is_actived?=1, XLOOKUP($A#, Calc!$A$#:$A$####, Calc!$AB$#:$AB$####, 0, 0, 2), 0)`
- **7,762** × `F#*C#`
- **7,762** × `F#/(k_factor*Kpp)*Delta`
- **7,762** × `MIN(B#, H#)`
- **7,762** × `I#*D#*Kpp`
- **7,762** × `I#*PCL`
- **7,762** × `I#*CDPPAdv`
- **7,762** × `B#-I#`
- **7,762** × `M# * XLOOKUP(E#, RetailTariff[Voltage Level], CHOOSECOLS(RetailTariff[], IF(DPPA_Connection_Voltage_Level=##, #, #)))`
- **7,762** × `J#+K#+L#+N#`

## Notes
- `#` indicates row numbers normalized for pattern matching.
- DPPA is largely hourly, formula-driven columns referencing **Calc** and **SimulationData**.
