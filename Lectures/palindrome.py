'''
Name: Marcos Villarreal
Date: 03/30/22

This program will determine if an inputed string is a palindrome (same forwards and backwards)
'''
def input_name():
    firstname = input("Please enter your first name: ")
    return firstname

def greet_player(first_name):
    print(f"Welcome {first_name} to our program.")
    print(f"This will determine if a string is a palindrome (same forwards and backwards).")

def input_string():
    inputed_string = input("Please enter a string to check if it is a palindrome: ")
    return inputed_string

def is_palindrome(in_string):
    in_string = in_string.lower()
    back_string = in_string[::-1]
    if (in_string == back_string):
        #print("Your string is a palindrome.")
        return True
    else:
        #print("Your string is NOT a palindrome")
        return False

    '''with "for" loops'''
    #for ch in range(len(in_string)//2):
    #    if (in_string[ch] != in_string[-ch-1]):
    #        print("This is not a palindrome")
    #        break
    #else: 
    #    print("Your string is a palindrome")

def tests():
    assert is_palindrome("racecar") == True
    assert is_palindrome("superman") == False
    print("All test cases passed!")

def main():
    tests()
    first_name = input_name()
    greet_player(first_name)

    in_string = input_string()
    is_pali = is_palindrome(in_string)
    if (is_pali):
        print(f"Your string '{in_string}' is a palindrome")
    else:
        print(f"Your string '{in_string}' is NOT a palindrome")

if __name__ == "__main__":
    main()