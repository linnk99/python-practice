name = input("My name is... ")
age = int(input("And my age is... "))
times_printed = int(input("How many times you want the result printed? "))

turns_100 = 2019 + (100 - age)

for i in range(0, times_printed):
    print("\nYour name is " + name + " and you are " + str(age) + " years old")
    print("You\'ll turn 100 years old in the year " + str(turns_100))