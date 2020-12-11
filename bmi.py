# BMI Calculator
def bmi(height, weight, h_system, w_system):
    # Conversions if needed
    if h_system == "metric":
        height = height
    if h_system == "imperial":
        height = height / .39370
    if w_system == "metric":
        weight = weight
    if w_system == "imperial":
        weight = weight / 2.2046

    # BMI, metric formula
    bmi = round((weight / height / height) * 10000, 1)

    # BMI Outputs
    if bmi <= 18.5:
        return bmi, "Underweight"
    if bmi > 18.5 and bmi < 25:
        return bmi, "Healthy Weight"
    if bmi > 25 and bmi < 30:
        return bmi, "Overweight"
    if bmi > 30:
        return bmi, "Obese"


# BMR Calculator, to determine daily calories
def bmr(height, weight, age, sex, activity, h_system, w_system):
    # Conversions if needed
    if h_system == "metric":
        height = height
    if h_system == "imperial":
        height = height / .39370
    if w_system == "metric":
        weight = weight
    if w_system == "imperial":
        weight = weight / 2.2046

    # BMI, metric
    bmi = round((weight / height / height) * 10000, 1)

    # Baseline BMRs, using the Revised Harris-Benedict Equation
    bmr_men = round(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age))
    bmr_women = round(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age))

    # Calories needed per day to maintain/lose/gain weigh, depending on activity level
    # If Men
    if sex == 'm':
        if activity == 0:  # Baseline
            return bmr_men, 0, 0
        if activity == 1:  # Sedentary
            bmr_men_1 = round(bmr_men * 1.2)
            bmr_men_1_lose = round(bmr_men_1 - 500)
            bmr_men_1_gain = round(bmr_men_1 + 500)
            return bmr_men_1, bmr_men_1_lose, bmr_men_1_gain
        if activity == 2:  # Lightly Active
            bmr_men_2 = round(bmr_men * 1.375)
            bmr_men_2_lose = round(bmr_men_2 - 500)
            bmr_men_2_gain = round(bmr_men_2 + 500)
            return bmr_men_2, bmr_men_2_lose, bmr_men_2_gain
        if activity == 3:  # Moderately Active
            bmr_men_3 = round(bmr_men * 1.55)
            bmr_men_3_lose = round(bmr_men_3 - 500)
            bmr_men_3_gain = round(bmr_men_3 + 500)
            return bmr_men_3, bmr_men_3_lose, bmr_men_3_gain
        if activity == 4:  # Very Active
            bmr_men_4 = round(bmr_men * 1.725)
            bmr_men_4_lose = round(bmr_men_4 - 500)
            bmr_men_4_gain = round(bmr_men_4 + 500)
            return bmr_men_4, bmr_men_4_lose, bmr_men_4_gain
        if activity == 5:  # Extra Active
            bmr_men_5 = round(bmr_men * 1.9)
            bmr_men_5_lose = round(bmr_men_5 - 500)
            bmr_men_5_gain = round(bmr_men_5 + 500)
            return bmr_men_5, bmr_men_5_lose, bmr_men_5_gain

    # If Women
    if sex == 'f':
        if activity == 0:
            return bmr_women, 0, 0
        if activity == 1:
            bmr_women_1 = round(bmr_women * 1.2)
            bmr_women_1_lose = round(bmr_women_1 - 500)
            bmr_women_1_gain = round(bmr_women_1 + 500)
            return bmr_women_1, bmr_women_1_lose, bmr_women_1_gain
        if activity == 2:
            bmr_women_2 = round(bmr_women * 1.375)
            bmr_women_2_lose = round(bmr_women_2 - 500)
            bmr_women_2_gain = round(bmr_women_2 + 500)
            return bmr_women_2, bmr_women_2_lose, bmr_women_2_gain
        if activity == 3:
            bmr_women_3 = round(bmr_women * 1.55)
            bmr_women_3_lose = round(bmr_women_3 - 500)
            bmr_women_3_gain = round(bmr_women_3 + 500)
            return bmr_women_3, bmr_women_3_lose, bmr_women_3_gain
        if activity == 4:
            bmr_women_4 = round(bmr_women * 1.725)
            bmr_women_4_lose = round(bmr_women_4 - 500)
            bmr_women_4_gain = round(bmr_women_4 + 500)
            return bmr_women_4, bmr_women_4_lose, bmr_women_4_gain
        if activity == 5:
            bmr_women_5 = round(bmr_women * 1.9)
            bmr_women_5_lose = round(bmr_women_5 - 500)
            bmr_women_5_gain = round(bmr_women_5 + 500)
            return bmr_women_5, bmr_women_5_lose, bmr_women_5_gain
