import os

loop = True
while True:

    arr = ["Smartphone","Tablet","Laptop","Headphones","PC"]

    print("Items for sale:" + "\n\n1 - Smartphone" + "\n2 - Tablet" + "\n3 - Laptop" + "\n4 - Headphones" + "\n5 - PC")

    choice = int(input("\nWhich item would you like to buy? "))

    if choice == 1: 
        print (arr[0])

    elif  choice == 2: 
        print (arr[1])

    elif choice == 3: 
        print (arr[2])

    elif choice == 4: 
        print (arr[3])

    elif choice == 5: 
        print (arr[4])

    else: 
        print ("Invalid input!")

    os.system("pause")  

    retry = input("\nTry again? (y/n): ")
    if retry.lower() != "y":
        break  






