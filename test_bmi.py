import pytest
from BMI import calculate_bmi

# ── Underweight 
def test_underweight_clear():
    # 5'5" (65 in), 100 lbs → well below 18.5
    bmi, group = calculate_bmi(100, 65)
    assert group == "underweight"
    
def test_underweight_upper_boundary():
    # BMI of 18.4 → still underweight
    bmi, group = calculate_bmi(107, 65)
    assert group == "underweight"

# ── Normal Weight
def test_normal_lower_boundary():
    # BMI of exactly 18.5 → normal weight
    bmi, group = calculate_bmi(112, 65)
    assert group == "normal weight"

def test_normal_clear():
    # 5'3" (63 in), 125 lbs → 22.7 per the teacher's own example
    bmi, group = calculate_bmi(125, 63)
    assert group == "normal weight"

def test_normal_upper_boundary():
    # BMI of 24.7 → still normal weight
    bmi, group = calculate_bmi(145, 65)
    assert group == "normal weight"

# ── Overweight 
def test_overweight_lower_boundary():
    # BMI of 25.0 → overweight
    bmi, group = calculate_bmi(169, 65)
    assert group == "overweight"

def test_overweight_clear():
    bmi, group = calculate_bmi(156, 65)
    assert group == "overweight"

def test_overweight_upper_boundary():
    # BMI of 29.8 → still overweight
    bmi, group = calculate_bmi(175, 65)
    assert group == "overweight"

# ── Obese 
def test_obese_lower_boundary():
    # BMI of 30.0 → obese
    bmi, group = calculate_bmi(176, 65)
    assert group == "obese"

def test_obese_clear():
    bmi, group = calculate_bmi(250, 65)
    assert group == "obese"

# ── BMI value accuracy 
def test_bmi_value_example_from_instructions():
    # Teacher's own example: 5'3", 125 lbs → 22.7
    bmi, _ = calculate_bmi(133, 65)
    assert bmi == 22.7

def test_bmi_rounded_to_one_decimal():
    bmi, _ = calculate_bmi(140, 65)
    assert bmi == round(bmi, 1)