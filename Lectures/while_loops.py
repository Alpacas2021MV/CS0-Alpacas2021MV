def main():
    keepRunning = True
    while (keepRunning):
        number = input("Please enter a whole number: ")
        if (number.isnumeric() == True):
            print(f"You entered a whole number. COngratulations!")
            keepRunning = False
        else:
            print(f"You must enter a whole number, try again :( ")

    print(f"Your number is {int(number)}")

main()