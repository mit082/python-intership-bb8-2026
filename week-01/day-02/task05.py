height_cm = "175"
weight_kg = "68.5"

height_cm = int(height_cm)
weight_kg = float(weight_kg)

height_m = height_cm / 100

bmi = weight_kg / (height_m * height_cm)

print("Height:", height_m, "meters")
print("Weight:", weight_kg, "kg")
print("Your BMI is:", bmi)