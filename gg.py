def calculate(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
           return num1 / num2
        else:
            return "math error"
    else:
        return "invalid operation"
    
num1 = float(input("num1:"))
num2 = float(input("num2:"))
operation = (input("choose operation:")) 

result = calculate(num1,num2,operation)
print(f"Result is{result}")



    
    

      
