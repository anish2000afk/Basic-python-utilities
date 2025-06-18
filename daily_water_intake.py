def calculate_water_intake(weight_kg, height_cm, gender):
    """
    Estimate daily water intake in liters based on weight, height, and gender.
    """
    # Base water need (in mL): 30–40 mL per kg is typical
    base_water_ml = weight_kg * 35

    # Adjust for gender (men tend to have more lean mass, hence slightly higher needs)
    if gender.lower() == "male":
        base_water_ml += 300  # extra ~300 ml
    elif gender.lower() == "female":
        base_water_ml += 0  # neutral
    else:
        base_water_ml += 150  # average value for nonbinary/others

    # Add a height factor (optional but helps refine for tall builds)
    if height_cm > 180:
        base_water_ml += 250
    elif height_cm < 150:
        base_water_ml -= 150

    # Convert to liters and round
    return round(base_water_ml / 1000, 2)


# 🧪 Example:
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): "))
gender = input("Enter your gender (male/female/other): ")

water_needed = calculate_water_intake(weight, height, gender)
print(f"\n💧 You should drink approximately {water_needed} liters of water per day.")


calculate_water_intake(55, 170, "male")
