def add(P, Q):
    return P + Q
def subtract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def divide(P, Q):
    return P / Q
print("Select operation (a/b/c/d): ")
print("a. Add")
print("b. subtract")
print("c. multiply")
print("d. divide")
choice = input("Enter choice: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice=="a":
    print(add(num1 , num2))
elif choice=="b":
    print(subtract(num1,num2))
elif choice=="c":
    print(multiply(num1,num2))
elif choice=="d":
    print(divide(num1,num2))
else:
    print("invalid input")