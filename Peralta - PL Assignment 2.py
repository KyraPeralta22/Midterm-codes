num = input("Enter elements: ")
arr = num.split()

print(arr)

for i in range(len(arr)):
    arr[i] = int(arr[i])

print("Sum = ", sum(arr))

    


