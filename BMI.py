def calculate_bmi(weight, height):
    weightpounds = weight * 0.45
    heightinches = height * 0.025
    bmi = weightpounds / (heightinches ** 2)
    rounded_bmi = round(bmi, 1)
    
    if rounded_bmi < 18.5:
        group = "underweight"
    elif 18.5 <= rounded_bmi < 24.9:
        group = "normal weight"
    elif 25 <= rounded_bmi < 29.9:
        group = "overweight"
    else:
        group = "obese"
    return rounded_bmi, group