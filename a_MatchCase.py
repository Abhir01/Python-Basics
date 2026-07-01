a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

match op:
    case "+":
        print(a+b)
    case "-":
        # print(sub(a, b))
        print(a-b)
    case "*":
        # print(mul(a, b))
        print(a*b)
    case "/":
        if b == 0:
            print("Cannot divide by zero")
        else:
            # print(div(a, b))
            print(a/b)
    case _:
        print("Invalid operation")