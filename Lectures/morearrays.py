import copy 

def mod_numbers(numbers):
    for i in range(len(numbers)):
        numbers[i]+= 10
    return (1, 2, 3)

def main():
    nums = input("Please enter 5 numbers separated by a space: ")
    nums = nums.split()

    #blimps = [input() for i in range(5)]
    #int_nums = []

    nums = [int(i) for i in nums]
    print(nums)

    nums.sort()

    print(nums)

    nums = [str(i) for i in nums]

    somestring = ' '.join(nums)
    
    print(somestring)
    #for element in nums:
    #    nums.append(int(element))
    #nums = nums[5:]
    #print(nums)
    #nums.sort(reverse =True)

main() 