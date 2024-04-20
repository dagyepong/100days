height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# BMI = weight(kg) / height2(m2)
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
if bmi_as_int < 18.5:
    print(f"Your bmi is {bmi_as_int}, you are underweight. ")
elif bmi_as_int < 25:
    print(f"Your bmi is {bmi_as_int}, you have a normal weight. ")
elif bmi_as_int < 30:
    print(f"Your bmi is {bmi_as_int}, you are overweight. ")
elif bmi_as_int < 35:
    print(f"Your bmi is {bmi_as_int}, you are obese. ")
else:
    print(f"Your bmi is {bmi_as_int}, you are clinically obese. ")
    
