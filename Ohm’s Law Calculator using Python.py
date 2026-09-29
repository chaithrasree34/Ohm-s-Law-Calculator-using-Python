# Ohm-s-Law-Calculator-using-Python
# Ohm's Law Calculator
# Formula: V = I * R

print("===== Ohm's Law Calculator =====")
print("1. Calculate Voltage (V)")
print("2. Calculate Current (I)")
print("3. Calculate Resistance (R)")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    current = float(input("Enter Current (I) in Amperes: "))
    resistance = float(input("Enter Resistance (R) in Ohms: "))
    voltage = current * resistance
    print("Voltage (V) =", voltage, "V")

elif choice == 2:
    voltage = float(input("Enter Voltage (V) in Volts: "))
    resistance = float(input("Enter Resistance (R) in Ohms: "))
    current = voltage / resistance
    print("Current (I) =", current, "A")

elif choice == 3:
    voltage = float(input("Enter Voltage (V) in Volts: "))
    current = float(input("Enter Current (I) in Amperes: "))
    resistance = voltage / current
    print("Resistance (R) =", resistance, "Ω")

else:
    print("Invalid choice! Please select 1, 2, or 3.")
