import random

def hint_match(expectedNumber:int)-> str: 
    ans =""
    user_input = []
    print("The number is:",expectedNumber)
    prompt = "Enter a value: "
    for i in range (0,7):
        user_input_str = input(prompt)
        try:
            user_input = int(user_input_str) 
        except ValueError:
            print("Invalid input. Please enter an integer.")
        if user_input != expectedNumber:
            print ("user_input", user_input)
        else:
            ans = "Yes you got it"
            return ans
    ans = "Limit is 7 , so finished!!"
    return ans

def generateRandomNumberOfRange(begin:int,end:int) -> int:
    data = random.randint(begin,end)
    print("The data is:", data)
    return data

print(hint_match(generateRandomNumberOfRange(0,20)))