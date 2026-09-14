def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a value greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

print("=" * 35)
print("       BMI CALCULATOR")
print("=" * 35)

while True:
    weight = get_positive_number("Enter your weight in kg: ")
    height = get_positive_number("Enter your height in meters: ")

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"\nYour BMI: {bmi:.2f}")
    print(f"Category: {category}")

    again = input("\nCalculate again? (y/n): ").strip().lower()
    if again != "y":
        print("Thank you for using the BMI Calculator!")
        break
