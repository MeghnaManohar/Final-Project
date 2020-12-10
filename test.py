import pytest
from bmi import *

@pytest.mark.parametrize('height, weight, age, sex, activity, h_system, w_system',
                         [
                             (180, 60, 22,'m', 2, 'metric', 'metric'),
                             (60.1, 118.9, 'f',22, 3, 'imperial', 'imperial'),
                         ])
def test_calculator(height, weight, age, sex, activity, h_system, w_system):
   m = calculator(height = float(height), weight = float(weight), age= float(age), sex = str(sex), activity = int(activity), h_system = str(h_system), w_system = str(w_system))
   
   assert True