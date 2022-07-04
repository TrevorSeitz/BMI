"""
Detail about BMI: https://en.wikipedia.org/wiki/Body_mass_index

BMI is calculated using a persons weight and height. BMI is 'weight' devided by square of height.

BMI = weight/(height^2)

The BMI should be classified as follows
Underweight - BMI under or equal to 18.5
Normal - BMI between 18.5 and 25 (not including 18.5 but including 25)
Overweight - BMI between- 25 and 30 (not including 25 but including 30)
Obese - BMI greater than 30

e.g. Input: weight(kg) - 60
            height(m) - 1.9
     Output: Your BMI is 16.6. You are Underweight.

e.g. Input: weight(kg) - 72
            height(m) - 1.84
     Output: Your BMI is 21.3. You are Normal.

e.g. Input: weight(kg) - 72
            height(m) - 1.6
     Output: Your BMI is 27.3. You are Overweight.

e.g. Input: weight(kg) - 70
            height(m) - 1.5
     Output: Your BMI is 31.1. You are Obese.
"""
from Get_Inputs import getinputs
from Calculate import calculate
from Give_Output import Give_BMI

bmiNumbers = getinputs()
weight = bmiNumbers[0]
height = bmiNumbers[1]
bmi = calculate(weight, height)
Give_BMI(bmi)

# bmiNumbers = Get_Inputs.getinputs()
# bmi = Calculate.calculate(bmiNumbers[0], bmiNumbers[1])
# bmi = Calculate
# Give_Output

# bmi = Calculate.calculate(bmiNumbers[0], bmiNumbers[1]).Give_BMI(bmi)

# def getinputs():
#      weight = input("What is your weight in kg? ")
#      height = input("What is your height in M? ")
#      # return weight, height
#      caculate(weight, height)

# def calculate(weight, height):
#      # print("Welcome to the BMI Calculator")
#      # weight = input("What is your weight in kg? ")
#      # height = input("What is your height in M? ")
#      bmiInputs =Get_Inputs()
#      weight = bmiInputs.weight
#      height = bmiInputs.height
#      print("Your BMI is", bmiInputs)
#      bmi = float(weight) / (float(height) ** 2)
#      bmi = round(bmi, 1)
#      return bmi

# getinputs()