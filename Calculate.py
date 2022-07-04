def calculate(weight, height):
     bmi = float(weight) / (float(height) ** 2)
     bmi = round(bmi, 1)
     return bmi