#gets user input
maxNum = int(input("What should the highest number be? "))
#desides the highest number to go up to based on the user input
for i in range(maxNum+1):
    #detcts if the number is divisible by 3 and prints based on it
    if i % 3 == 0:
        print("Fizzbuzz")
    else:
        print(i)