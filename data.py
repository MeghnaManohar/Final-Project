import pandas as pd

# Data for Exercise Table
df = pd.read_csv('exercise_data.csv')

# Data for Energy Table
df = pd.read_csv('energy_data.csv')

#Calorie counter dataset
FOOD_DATA = "Food_Display_Table.csv"

foodData_df = pd.read_csv(FOOD_DATA)
foodData_df = foodData_df.drop(columns=["Food_Code", "Portion_Default", "Factor", "Increment", "Multiplier"])


if __name__ == '__main__':
    pass