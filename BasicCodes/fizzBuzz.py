def basic_loop(n:int) -> list[str]:
    for i in range (n):
        print (i)
# basic_loop(3)


def print_Char(c:str):
    for char in c:
        print(char)
# print_Char("String")


def print_Dict(person):
    for key in person:
        print(f"key {key}, value {person[key]}")
person = {
    "name": "John",
    "age":30,
    "city":"Dhaka"
}
# print_Dict(person)


def fizz_buzz_begin(n:int)-> list[str]:
    list_of_string = []
    for i in range (n):
        list_of_string.append(str(i)) 
    return list_of_string

# print(fizz_buzz_begin(5))


def fizz_buzz(n:int)-> list[str]:
    list_of_string = []
    # Adjust range to typically start from 1 and include 'n'
    for i in range (1, n + 1): 
        # Use logical 'and' and check explicitly if both conditions are True
        if (i % 3 == 0) and (i % 5 == 0): 
            list_of_string.append("FizzBuzz")
        elif i % 3 == 0 :
            list_of_string.append("Fizz")
        elif i % 5 == 0 :
            list_of_string.append("Buzz")
        
        else:
            list_of_string.append(str(i))
    return list_of_string

print(fizz_buzz(20))
