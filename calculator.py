


print("You can do the following mathematical operations with BRILLIANT-CALCLATOR APP")
print("1.Addition\t2.Subtraction\t3.Multiplication\t4.Division\n5.Average")
choice = int(input("Enter Your choice:\n"))
condition = 'Y'
while condition == 'Y':
    if choice == 1:
        decision = 0
        while decision < 1:
            list = []
            i = 0

            n = int(input("how many no you want to sum:"))

            while (i < n):
                print("enter number")
                element = float(input())
                list.append(element)
                i += 1
            print(list)
            sum = 0
            for item in range(0, len(list)):
                sum = sum + list[item]
            print("Sum of the items:", sum)
            print("\nDo you want to add another number?")
            add_choice = int(input("What do you want to do?\n\t1.Addition\n\t2.Exit program"))
            if add_choice == 1:
                decision = 0
            elif add_choice == 2:
                sys.exit("\n---------Program exiting after addition operation!!!---------")

    elif choice == 2:
        print("You choose a Subtraction.")
        decision = 0
        while decision < 1:
            first_number = input("Enter first number:\n")
            second_number = input("Enter second number:\n")
            subtraction = float(first_number) - float(second_number)
            print("Result of the subtraction operation:\n\tFinal Result=", subtraction)
            print("Do you want to subtract another number?")
            sub_choice = int(input("What do you want to do?\n\t1.Subtraction\n\t2.Exit program"))
            if sub_choice == 1:
                decision = 0
            elif sub_choice == 2:
                sys.exit("\n---------Program exiting after Subtraction operation!!!---------")

    elif choice == 3:
        print("You choose a Multiplication.")
        decision = 0
        while decision < 1:
            list = []
            i = 0

            n = int(input("how many no you want to multiply:\n"))
            while (i < n):
                print("enter another item of the list")
                element = float(input())
                list.append(element)
                i += 1
            print(list)
            product = 1
            for item in range(0, len(list)):
                product = product * list[item]
            print("Product of the numbers:", product)
            print("Do you want to multiply another number?")
            mul_choice = int(input("What do you want to do?\n\t1.Multiplication\n\t2.Exit program"))
            if mul_choice == 1:
                decision = 0
            elif mul_choice == 2:
                sys.exit("\n---------Program exiting after addition operation!!!---------")

    elif choice == 4:
        print("You choose division operation.")
        decision = 0
        while decision < 1:
            divident = input("enter Divident:\n")
            divisor = input("Enter Divisor:\n")
            result = int(divident) / int(divisor)
            reminder = int(divident) % int(divisor)
            print("\nResult of the division operation:\n\tquotent       :", int(result), "\n\treminder      :",
                  reminder)
            print("Do you want to divide another number?")
            div_choice = int(input("What do you want to do?\n\t1.Division\n\t2.Exit program"))
            if div_choice == 1:
                decision = 0
            elif div_choice == 2:
                sys.exit("---------Program Exiting after division operation!!!---------")

    elif choice == 5:
        print("You choose to calculate average value of the number.\nEnter numbers whose average you want to calculate:")
        decision = 0
        while decision < 1:
            list = []
            i = 0
            n = int(input("how many no you want to average:"))
            while (i < n):
                print("enter item of the list")
                element = float(input())
                list.append(element)
                i += 1
            print(list)
            sum = 0
            for item in range(0, len(list)):
                sum = sum + list[item]
            print("The average of the numbers is:", sum / n)
            print("Do you want to perform another Average Operation?")
            avg_choice = int(input("What do you want to do?\n\t1.Average\n\t2.Exit program"))
            if avg_choice == 1:
                decision = 0
            elif avg_choice == 2:
                sys.exit("---------Program exiting after Average calculation!!!--------")
    else:
        print("Invalid input!!!\nChoose integer value from 1 to 8.")
        condition = 'F'

sys.exit("\nThank you ")
