height = 1.8
weight = 65
bmi = weight/height**2

print(f"BMI is {bmi}")
if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normal weight")
elif bmi>= 25 and bmi<= 29.9:
    print("overweight")
else:
    print("Obese")

if 10 == 10.00:
    print("Equal")
else:
    print("Not Equal")

sentence = "kenya, Uganda and Tanzania"
if "kenya" in sentence.lower():
    print("Yes, it exists")
else:
    print("Does not exists")