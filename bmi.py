#This uses the metric system
def calculator(height, weight, age, sex, activity):
    #BMI, metric
    bmi = round((weight/height/height) * 10000,1)
    
    #Baseline BMRs, using the Revised Harris-Benedict Equation
    bmr_men = round(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age))
    bmr_women = round(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age))
       
    #If Men
    if sex == 'm':
        if activity == 0:
            return bmi, bmr_men, 0, 0
        if activity == 1:
            bmr_men_1 = round(bmr_men *1.2)
            bmr_men_1_lose = round(bmr_men_1 - 1000)
            bmr_men_1_gain = round(bmr_men_1 + 1000)
            return bmi, bmr_men_1, bmr_men_1_lose, bmr_men_1_gain
        if activity == 2:
            bmr_men_2 = round(bmr_men *1.375)
            bmr_men_2_lose = round(bmr_men_2 - 1000)
            bmr_men_2_gain = round(bmr_men_2 + 1000)
            return bmi, bmr_men_2, bmr_men_2_lose, bmr_men_2_gain  
        if activity == 3:
            bmr_men_3 = round(bmr_men *1.55)
            bmr_men_3_lose = round(bmr_men_3 - 1000)
            bmr_men_3_gain = round(bmr_men_3 + 1000)     
            return bmi, bmr_men_3, bmr_men_3_lose, bmr_men_3_gain
        if activity == 4:
            bmr_men_4 = round(bmr_men *1.725)
            bmr_men_4_lose = round(bmr_men_4 - 1000)
            bmr_men_4_gain = round(bmr_men_4 + 1000)
            return bmi, bmr_men_4, bmr_men_4_lose, bmr_men_4_gain
        if activity == 5:
            bmr_men_5 = round(bmr_men *1.9)
            bmr_men_5_lose = round(bmr_men_5 - 1000)
            bmr_men_5_gain = round(bmr_men_5 + 1000)
            return bmi, bmr_men_5, bmr_men_5_lose, bmr_men_5_gain       
    #If Women
    if sex =='f':
        if activity == 0:
            return bmi, bmr_women, 0, 0
        if activity == 1:
            bmr_women_1 = round(bmr_women *1.2)
            bmr_women_1_lose = round(bmr_women_1 - 1000)
            bmr_women_1_gain = round(bmr_women_1 + 1000)
            return bmi, bmr_women_1, bmr_women_1_lose, bmr_women_1_gain
        if activity == 2:
            bmr_women_2 = round(bmr_women *1.375)
            bmr_women_2_lose = round(bmr_women_2 - 1000)
            bmr_women_2_gain = round(bmr_women_2 + 1000)
            return bmi, bmr_women_2,bmr_women_2_lose, bmr_women_2_gain
        if activity == 3:
            bmr_women_3 = round(bmr_women *1.55)
            bmr_women_3_lose = round(bmr_women_3 - 1000)
            bmr_women_3_gain = round(bmr_women_3 + 1000)
            return bmi, bmr_women_3, bmr_women_3_lose, bmr_women_3_gain
        if activity == 4:
            bmr_women_4 = round(bmr_women *1.725)
            bmr_women_4_lose = round(bmr_women_4 - 1000)
            bmr_women_4_gain = round(bmr_women_4 + 1000)
            return bmi, bmr_women_4, bmr_women_4_lose, bmr_women_4_gain
        if activity == 5:
            bmr_women_5 = round(bmr_women *1.9)
            bmr_women_5_lose = round(bmr_women_1 - 1000)
            bmr_women_5_gain = round(bmr_women_1 + 1000)
            return bmi, bmr_women_5, bmr_women_5_lose, bmr_women_5_gain


#This uses the imperial system
def calculator_imperial(height, weight, age, sex, activity):
    #BMI, imperial system
    bmi = round(weight/(height*height) * 703,1)
    
    #Conversions for BMR formula
    h = height/.39370
    w = weight/2.2046
    
    #Baseline BMRs, using the Revised Harris-Benedict Equation
    bmr_men = round(88.362 + (13.397 * w) + (4.799 * h) - (5.677 * age))
    bmr_women = round(447.593 + (9.247 * w) + (3.098 * h) - (4.330 * age))
       
    #If Men
    if sex == 'm':
        if activity == 0:
            return bmi, bmr_men, 0, 0
        if activity == 1:
            bmr_men_1 = round(bmr_men *1.2)
            bmr_men_1_lose = round(bmr_men_1 - 1000)
            bmr_men_1_gain = round(bmr_men_1 + 1000)
            return bmi, bmr_men_1, bmr_men_1_lose, bmr_men_1_gain
        if activity == 2:
            bmr_men_2 = round(bmr_men *1.375)
            bmr_men_2_lose = round(bmr_men_2 - 1000)
            bmr_men_2_gain = round(bmr_men_2 + 1000)
            return bmi, bmr_men_2, bmr_men_2_lose, bmr_men_2_gain  
        if activity == 3:
            bmr_men_3 = round(bmr_men *1.55)
            bmr_men_3_lose = round(bmr_men_3 - 1000)
            bmr_men_3_gain = round(bmr_men_3 + 1000)     
            return bmi, bmr_men_3, bmr_men_3_lose, bmr_men_3_gain
        if activity == 4:
            bmr_men_4 = round(bmr_men *1.725)
            bmr_men_4_lose = round(bmr_men_4 - 1000)
            bmr_men_4_gain = round(bmr_men_4 + 1000)
            return bmi, bmr_men_4, bmr_men_4_lose, bmr_men_4_gain
        if activity == 5:
            bmr_men_5 = round(bmr_men *1.9)
            bmr_men_5_lose = round(bmr_men_5 - 1000)
            bmr_men_5_gain = round(bmr_men_5 + 1000)
            return bmi, bmr_men_5, bmr_men_5_lose, bmr_men_5_gain       
    #If Women
    if sex =='f':
        if activity == 0:
            return bmi, bmr_women, 0, 0
        if activity == 1:
            bmr_women_1 = round(bmr_women *1.2)
            bmr_women_1_lose = round(bmr_women_1 - 1000)
            bmr_women_1_gain = round(bmr_women_1 + 1000)
            return bmi, bmr_women_1, bmr_women_1_lose, bmr_women_1_gain
        if activity == 2:
            bmr_women_2 = round(bmr_women *1.375)
            bmr_women_2_lose = round(bmr_women_2 - 1000)
            bmr_women_2_gain = round(bmr_women_2 + 1000)
            return bmi, bmr_women_2,bmr_women_2_lose, bmr_women_2_gain
        if activity == 3:
            bmr_women_3 = round(bmr_women *1.55)
            bmr_women_3_lose = round(bmr_women_3 - 1000)
            bmr_women_3_gain = round(bmr_women_3 + 1000)
            return bmi, bmr_women_3, bmr_women_3_lose, bmr_women_3_gain
        if activity == 4:
            bmr_women_4 = round(bmr_women *1.725)
            bmr_women_4_lose = round(bmr_women_4 - 1000)
            bmr_women_4_gain = round(bmr_women_4 + 1000)
            return bmi, bmr_women_4, bmr_women_4_lose, bmr_women_4_gain
        if activity == 5:
            bmr_women_5 = round(bmr_women *1.9)
            bmr_women_5_lose = round(bmr_women_1 - 1000)
            bmr_women_5_gain = round(bmr_women_1 + 1000)
            return bmi, bmr_women_5, bmr_women_5_lose, bmr_women_5_gain