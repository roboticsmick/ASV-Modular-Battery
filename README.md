# ASV-Modular-Battery

## Target 

1. Design a battery cell configuration that is under 100wh so it can be safely carried on all commericial planes without restrictions.
2. Is above 12V and under 20V to work in the operating range of COTS regulators used in ASV and AUV.
3. Maximised for endurance (Ah) and continous current draw (A). 

## Battery Results

### Sanyo NCR20700A 3200mAh 30A Battery

Single 4S2P Battery Pack Specifications:
Nominal Voltage: 14.4V
Capacity: 6.4Ah
Watt Hours: 92.16Wh
Max Current Draw: 60A

Two 4S2P Battery Packs in Parallel Specifications:
Nominal Voltage: 14.4V
Total Capacity: 12.8Ah
Total Watt Hours: 184.32Wh
Total Max Current Draw: 120A

### Molicel INR-20700A 3000mAh 35A Battery

Single 4S2P Battery Pack Specifications:
Nominal Voltage: 14.4V
Capacity: 6Ah
Watt Hours: 86.4Wh
Max Current Draw: 70A

Two 4S2P Battery Packs in Parallel Specifications:
Nominal Voltage: 14.4V
Total Capacity: 12Ah
Total Watt Hours: 172.8Wh
Total Max Current Draw: 140A

## Critical Considerations:
1. Ensure all cells are at the same voltage before connecting in parallel to avoid high current surges.
2. Use high-quality connectors and wires with appropriate gauge to handle the total current.
3. Implement a Battery Management System (BMS) to monitor and protect each cell and pack.
4. Ensure the charger matches the pack's voltage and capacity specifications, and has balancing capabilities.
5. Regularly check cell voltages, temperature, and overall pack health to prevent issues.
6. Secure all connections to avoid accidental disconnections or short circuits.
7. Use thermal sensors and fuses for additional safety measures.
8. When charging, use a smart charger that can balance the cells and avoid overcharging.
