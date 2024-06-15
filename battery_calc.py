# Battery cell specifications for Molicel INR-20700A
cell_voltage_nominal = 3.6  # Nominal voltage per cell (V)
cell_capacity_ah = 3  # Capacity per cell (Ah)
cell_max_current_a = 35  # Max current draw per cell (A)
series_cells = 4
parallel_cells = 2

# Calculations for a single 4S2P battery pack
pack_voltage_nominal = cell_voltage_nominal * series_cells
pack_capacity_ah = cell_capacity_ah * parallel_cells
pack_watt_hours = pack_voltage_nominal * pack_capacity_ah
pack_current_draw_a = cell_max_current_a * parallel_cells

# Display the results for a single pack
print(f"Single 4S2P Battery Pack Specifications:")
print(f"Nominal Voltage: {pack_voltage_nominal}V")
print(f"Capacity: {pack_capacity_ah}Ah")
print(f"Watt Hours: {pack_watt_hours}Wh")
print(f"Max Current Draw: {pack_current_draw_a}A")

# Connecting two 4S2P packs in parallel
total_voltage_nominal = pack_voltage_nominal  # Voltage remains the same
total_capacity_ah = pack_capacity_ah * 2  # Capacity doubles
total_watt_hours = pack_watt_hours * 2  # Watt hours double
total_current_draw_a = pack_current_draw_a * 2  # Current draw doubles

# Display the results for two packs in parallel
print(f"\nTwo 4S2P Battery Packs in Parallel Specifications:")
print(f"Nominal Voltage: {total_voltage_nominal}V")
print(f"Total Capacity: {total_capacity_ah}Ah")
print(f"Total Watt Hours: {total_watt_hours}Wh")
print(f"Total Max Current Draw: {total_current_draw_a}A")

# Critical considerations
critical_considerations = """
Critical Considerations:
1. Ensure all cells are at the same voltage before connecting in parallel to avoid high current surges.
2. Use high-quality connectors and wires with appropriate gauge to handle the total current.
3. Implement a Battery Management System (BMS) to monitor and protect each cell and pack.
4. Ensure the charger matches the pack's voltage and capacity specifications, and has balancing capabilities.
5. Regularly check cell voltages, temperature, and overall pack health to prevent issues.
6. Secure all connections to avoid accidental disconnections or short circuits.
7. Use thermal sensors and fuses for additional safety measures.
8. When charging, use a smart charger that can balance the cells and avoid overcharging.
"""

print(critical_considerations)
