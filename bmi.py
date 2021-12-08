def solve(**kwargs):
    return (kwargs['val1']/((kwargs['val2']/100)*(kwargs['val2']/100)))

#Defining variables and displays user instruction
weight=float(input("Enter your weight in kilograms:"))
height=float(input("Enter your height in centimeters:"))

# Calculate the BMI
bmi = solve(val1=weight, val2=height)
#print (f"Your BMI is: {bmi}")

# Display the result to the user
if bmi <= 18.4:
     print("You are underweight.")
elif bmi <= 24.9:
     print("You are normal weight.")
elif bmi <= 29.9:
     print("You are Overweight.")
elif bmi <= 34.9:
     print("You have Class I Obesity.")
elif bmi <= 39.9:
     print("You have Class II Obesity.")
else:
     print("You are Class III Obesity.")