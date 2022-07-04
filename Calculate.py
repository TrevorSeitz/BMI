def calculate(weight, height):
    #  bmiInputs =Get_Inputs()
    #  weight = bmiInputs.weight
    #  height = bmiInputs.height
    #  print("Your BMI is", bmiInputs)
     bmi = float(weight) / (float(height) ** 2)
     bmi = round(bmi, 1)
     return bmi