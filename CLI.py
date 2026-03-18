from BMI import calculate_bmi

def get_height_in_inches():
    feet = int(input("Enter height (feet): "))
    inches = int(input("Enter height (inches): "))
    return (feet * 12) + inches

def main():
    print("=== BMI Calculator ===")
    height = get_height_in_inches()
    weight = float(input("Enter weight (pounds): "))
    bmi, category = calculate_bmi(weight, height)
    print(f"\nYour BMI: {bmi}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
