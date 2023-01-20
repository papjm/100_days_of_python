bmi = round(weight / height**2)
if bmi < 18.5:
    print(f"your bmi is,{bmi} you are underwieght")
elif bmi < 25:
    print(f"your bmi is,{bmi} you have a normal weight")
elif bmi < 30:
    print(f"your bmi is,{bmi} you have are overweight")
elif bmi < 35:
    print(f"your bmi is,{bmi} you are obese")
elif bmi > 35:
    print(f"your bmi is,{bmi} you have are clinically obese")
