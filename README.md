# Final-Project: MP Health App
Creators: Meghna Manohar & Precious Ufomadu

Last Updated: December 10, 2020

Description:
Our Health App helps users live a healthier lifestyle! After obtaining information, the app outputs the user's BMI, BMR, and suggests daily calories depending on whether they want to maintain/lose/gain weight. Learn about common exercises and create your own daily menu!


Usage (for Users):
Users input their sex, weight, height, age, and activity levels (in metric system or in the imperial system). Our app will then output the user's Body Mass Index (BMI) and includes a visual of the ranges of BMI (from underweight to obese). Users will also see their Basal Metabolic Rate (BMR) which helps determine how many calories the user should have daily.  

Users can also search and filter through our common exercises database and see how many calories they'll burn by doing that activity for 1 hour. We've also included information about the amount calories from one gram (or ounce) from common food groups (like protein, carbs, fats, etc.). Users can also sort this table. 

Finally, users can create a menu for the day, by searching for through our food database. After selecting a few tasty items, our program will catalog how many calories each item of the menu has and total it up for the user. 


Usage (for Developers):
"health_app.py": contains the code for the app layout and to run on a Dash server. 
"bmi.py": contains code to run bmi and bmr calculations.
"energy_data.csv, exercise_date.csv, and Food_Display_Table.csv" are the databases used in our app

Notes:
Users' BMR is calculated using the revised Harris-Benedict Equation.
