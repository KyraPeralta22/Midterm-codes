class Test:

    def add(*args):
        sum = 0
        for i in args:
            try:
                sum += int(i)
            except Exception as error:
                print("Cannot add this value: ", error)
        return sum


    def sub(*args):
            diff = int(args[0])
            for i in args:
                try:
                    if args[0] == i:
                        continue
                    diff = diff - int(i)
                except Exception as error:
                    print("Cannot subtract this value: ", error)
            return diff

    def parse(input):
        list = input.split(",")
        return list

if __name__ == "__main__":

    try: 

        while True:
            print("\n1 - Addition\n2 - Subtraction")
            operator = input("Select an operator: ")

            if operator == "1":
                num = Test.parse(input("\nEnter a series of numbers you want to add (separate them using commas): "))
                print(Test.add(*num))

            elif operator == "2":
                num = Test.parse(input("\nEnter a series of numbers you want to subtract (separate them using commas):"))
                print(Test.sub(*num))

            else:
                print ("Invalid input!")

    except ValueError:
        print("Error. Invalid Input.")

