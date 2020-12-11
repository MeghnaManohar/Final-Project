import pytest
from bmi import *
from health_app import *


# Testing BMI Function
@pytest.mark.parametrize('height, weight, h_system, w_system',
                         [
                             (180, 165, 'metric', 'imperial'),
                             (152.4, 118.9, 'metric', 'imperial'),
                         ])
def test_bmi(height, weight, h_system, w_system):
    p = bmi(height=float(height), weight=float(weight), h_system=str(h_system), w_system=str(w_system))

    assert True


# Testing BMR Function
@pytest.mark.parametrize('height, weight, age, sex, activity, h_system, w_system',
                         [
                             (180, 60, 22, 'm', 2, 'metric', 'metric'),
                             (60.1, 118.9, 'f', 22, 3, 'imperial', 'imperial'),
                         ])
def test_bmr(height, weight, age, sex, activity, h_system, w_system):
    m = bmr(height=float(height), weight=float(weight), age=float(age), sex=str(sex), activity=int(activity),
            h_system=str(h_system), w_system=str(w_system))

    assert True

#test calorie addition function
@pytest.mark.parametrize("output",
                         [
                             ("Ice cream, rich - cup", "Soft serve ice cream - cup")
                         ])
def display_total_calories(output):
   x = display_total_calories(output)
   assert 716.25 == x


if __name__ == '__main__':
    pass

