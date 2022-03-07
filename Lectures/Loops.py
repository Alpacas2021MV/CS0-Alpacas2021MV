'''
Name: Marcos Villarreal
Date: 03/04/22

This is to demonstrate loops. This program determines whether a given number is prime or not. 
'''
def is_prime(number):
    for i in range(2, (number//2) +1):
        if (number%i == 0):
            return False, i
    else: 
        return True, 0

def print_result(prime, number, divisor):
    if not (prime):
        print(f"{number} is NOT prime")
        print(f"{number} is divisible by {divisor}")
    else:
        print(f"{number} is prime")

def tests(): 
    assert is_prime(42) == (False, 2)
    assert is_prime(13) == (True, 0)
    assert is_prime(47) == (True, 0)
    print("All test cases passed") 

def main():
    tests()
    #n = 13
    n = int(input("Please enter a whole number greater than 2: "))
    prime, divisor = is_prime(n)
    print_result(prime, n, divisor)


main()