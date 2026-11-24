y = int(input("Enter year: "))

if y % 400 == 0:
    print("Leap Year")
elif y % 100 == 0:
    print("Not a Leap Year")
elif y % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
