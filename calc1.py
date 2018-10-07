print("This is my first calculator app, built from scratch!")

#function calculateNumbers
def calculateNumbers(self, operation, number_one, number_two):
    print("Enter number one: ")
    number_one = input("Enter first number: ")
    print("Enter desired operation: ")
    operation = input("Enter operation: ")
    print("Enter number two: ")
    number_two = input("Enter second number: ")
    x = number_one
    y = number_two
    op = operation

# for each element in array
    if op == "-":
        result = x - y
        print(result)
    elif op == "-":
        result = x + y
        print(result)
    elif op == "*":
        result = x * y
        print(result)
    elif op == "/":
        result = (x / y)
        print(result);

#     check what calculation symbol they select
#         if symbol is add
#             add number1 and number2
#         if symbole is minus
#             minus numbers
#         if symbol is divide
#              divide numbers
#         if symbol if multiply
#              multiply numbers

# return result