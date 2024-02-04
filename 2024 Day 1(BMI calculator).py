'''BMI CALCULATOR'''
height_m = 1.59
weight_kg = 63
BMI =  weight_kg / height_m ** 2
print("BMI is : ")
print(BMI)
if BMI < 25 :
    print("The person is healthy")
elif BMI > 25 :
    print("The person is not healthy")
else :
    print("BMI is in perfect scale")
