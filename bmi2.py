class BMI:
    def __init__(self, height, weight, age, sex, activity):
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex
        self.activity = activity
      
    def calc(self):
        #BMI, using metric system
        height = self.height
        weight = self.weight
        age = self.age
        sex = self.sex
        activity = self.activity
        bmi = round((weight/height/height) * 10000,2)
        
        #Baseline BMRs, using the Revised Harris-Benedict Equation
        bmr_men = round(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age))
        bmr_women = round(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age))
    
            
        #BMI Outputs
        if bmi <= 18.5:
            print('Your BMI is:', bmi,"This means you're underweight.")
    
        elif bmi > 18.5 and bmi < 25:
            print('Your BMI is:', bmi,"This means you're in the normal range.")
    
        elif bmi > 25 and bmi < 30:
            print('Your BMI is:', bmi,"This means you're overweight")
    
        elif bmi > 30:
            print('Your BMI is:', bmi,"This means you're obese.")
    
        #If Men
        if sex == 'M' or 'm':
            if activity == 0:
                print ('To maintain your weight you need:', bmr_men, 'Kcal/day')
                return bmr_men
            if activity == 1:
                bmr_men_1 = round(bmr_men *1.2)
                bmr_men_1_lose = round(bmr_men_1 - 1000)
                bmr_men_1_gain = round(bmr_men_1 + 1000)
                return bmr_men_1, bmr_men_1_lose, bmr_men_1_gain
            if activity == 2:
                bmr_men_2 = round(bmr_men *1.375)
                bmr_men_2_lose = round(bmr_men_2 - 1000)
                bmr_men_2_gain = round(bmr_men_2 + 1000)
                print ('To maintain your weight you need:', bmr_men_2, 'Kcal/day')
                print('To lose 1 kg per week you need:', bmr_men_2_lose, 'Kcal/day')
                print('To gain 1 kg per week you need:', bmr_men_2_gain, 'Kcal/day')
                return bmr_men_2  
            if activity == 3:
                bmr_men_3 = round(bmr_men *1.55)
                bmr_men_3_lose = round(bmr_men_3 - 1000)
                bmr_men_3_gain = round(bmr_men_3 + 1000)
                print ('To maintain your weight you need:', bmr_men_3, 'Kcal/day')
                print('To lose 1 kg per week you need:', bmr_men_3_lose, 'Kcal/day')
                print('To gain 1 kg per week you need:', bmr_men_3_gain, 'Kcal/day')     
                return bmr_men_3
            if activity == 4:
                bmr_men_4 = round(bmr_men *1.725)
                bmr_men_4_lose = round(bmr_men_4 - 1000)
                bmr_men_4_gain = round(bmr_men_4 + 1000)
                print ('To maintain your weight you need:', bmr_men_4, 'Kcal/day')
                print('To lose 1 kg per week you need:', bmr_men_4_lose, 'Kcal/day')
                print('To gain 1 kg per week you need:', bmr_men_4_gain, 'Kcal/day')
                return bmr_men_4
            if activity == 5:
                bmr_men_5 = round(bmr_men *1.9)
                bmr_men_5_lose = round(bmr_men_5 - 1000)
                bmr_men_5_gain = round(bmr_men_5 + 1000)
                print ('To maintain your weight you need:', bmr_men_5, 'Kcal/day')
                print('To lose 1 kg per week you need:', bmr_men_5_lose, 'Kcal/day')
                print('To gain 1 kg per week you need:', bmr_men_5_gain, 'Kcal/day')
                return bmr_men_5       
        #If Women
        if sex == 'F' or'f':
            if activity == 0:
                print ('To maintain your weight you need:', bmr_women, 'Kcal/day')
                return bmr_women
            if activity == 1:
                bmr_women_1 = round(bmr_women *1.2)
                bmr_women_1_lose = round(bmr_women_1 - 1000)
                bmr_women_1_gain = round(bmr_women_1 + 1000)
                print ('To maintain your weight you need:', bmr_women_1, 'Kcal/day')
                print('To lose 1 kg per week you need:', bmr_women_1_lose, 'Kcal/day')
                print('To gain 1 kg per week you need:', bmr_women_1_gain, 'Kcal/day')
                return bmr_women_1
            if activity == 2:
                bmr_women_2 = round(bmr_women *1.375)
                bmr_women_2_lose = round(bmr_women_2 - 1000)
                bmr_women_2_gain = round(bmr_women_2 + 1000)
                print ('To maintain your weight you need:', bmr_women_2, 'Kcal/day')
                print('To lose 1 kg per week you need:', bmr_women_2_lose, 'Kcal/day')
                print('To gain 1 kg per week you need:', bmr_women_2_gain, 'Kcal/day')
                return bmr_women_2
            if activity == 3:
                bmr_women_3 = round(bmr_women *1.55)
                bmr_women_3_lose = round(bmr_women_3 - 1000)
                bmr_women_3_gain = round(bmr_women_3 + 1000)
                print ('To maintain your weight you need:', bmr_women_3, 'Kcal/day')
                print('To lose 1 kg per week you need:', bmr_women_3_lose, 'Kcal/day')
                print('To gain 1 kg per week you need:', bmr_women_3_gain, 'Kcal/day')
                return bmr_women_3
            if activity == 4:
                bmr_women_4 = round(bmr_women *1.725)
                bmr_women_4_lose = round(bmr_women_4 - 1000)
                bmr_women_4_gain = round(bmr_women_4 + 1000)
                print ('To maintain your weight you need:', bmr_women_4, 'Kcal/day')
                print('To lose 1 kg per week you need:', bmr_women_4_lose, 'Kcal/day')
                print('To gain 1 kg per week you need:', bmr_women_4_gain, 'Kcal/day')
                return bmr_women_4
            if activity == 5:
                bmr_women_5 = round(bmr_women *1.9)
                bmr_women_5_lose = round(bmr_women_1 - 1000)
                bmr_women_5_gain = round(bmr_women_1 + 1000)
                print ('To maintain your weight you need:', bmr_women_5, 'Kcal/day')
                print('To lose 1 kg per week you need:', bmr_women_5_lose, 'Kcal/day')
                print('To gain 1 kg per week you need:', bmr_women_5_gain, 'Kcal/day')
                return bmr_women_5
        #IF Error
        else:
            print('There is an error, please double check your inputs')
        
        return bmi
