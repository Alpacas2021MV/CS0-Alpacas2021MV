def greeting(): 
    print("Hello Marcos")

def calc_values(x):
    print(x**2*5)

def calc_more_values(x):
    answer= x**2*5
    return answer
x=5 
answer = calc_more_values(x)
print(answer)

x=42
answer = calc_more_values(answer)
print(answer)

x=523
answer = calc_more_values(answer)
print(answer)

#name = input("Please enter your name: ")
#print("Hello", name)
def prompt_name():
    input_string = input("Please enter your name: ")
    return input_string

def greet(name):
    print("Hello", name)

greet(prompt_name())

name=""
name= prompt_name()
greet(name)
greet(name)
greet(name)
