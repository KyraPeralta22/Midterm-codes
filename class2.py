class BMI:

    def solve(**kwargs):
        weight = kwargs['val1']
        height = kwargs['val2']
        return (kwargs['val1']/((kwargs['val2']/100)*(kwargs['val2']/100)))

    def bmiclassify(bmi):
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

    if __name__ == "__main__":
            try: 
                weight=float(input("Enter your weight in kilograms:"))
                height=float(input("Enter your height in centimeters:"))
                    
                bmi = solve(height = height, weight = weight)
                print(f"BMI: {bmi:.2f}")
                bmiclassify(bmi)
            except ValueError:
                print("Error. Invalid Input.")