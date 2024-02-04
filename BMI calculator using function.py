name1 = "Hasib"
height_m1 = 1.6
weight_kg1 = 55
name2 = "Ushno"
height_m2 = 1.62
weight_kg2 = 70
name3 = "Shehab"
height_m3 = 1.63
weight_kg3 = 55

def BMI_Calculator(name, height_m, weight_kg) :
    BMI = weight_kg / (height_m ** 2)
    print("BMI is : " ,BMI)
    if BMI > 25 :
        print(name + " is Overweight")
    else :
        print(name + " is Not overweight")

BMI_Calculator(name1, height_m1, weight_kg1)
BMI_Calculator(name2, height_m2, weight_kg2)
BMI_Calculator(name3, height_m3, weight_kg3)




