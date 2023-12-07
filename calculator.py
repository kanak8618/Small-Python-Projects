a = int(input("Enter number :- "))
b = int(input("Enter number :- "))

print("----Select option----")
print("1- Addition + ")
print("2- Substraction - ")
print("3- Multiplication * ")
print("4- Division / ")

c = input("Enter your choice : ")

match c:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case _ :
        print("Invalid choice ")
    