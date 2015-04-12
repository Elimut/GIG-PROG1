number = float(input("Input number: "))

if number < 0.001:
    print("Number is extra small.")
elif number < 1:
    print("Number is small.")
else:
    print("Number is normal.")
