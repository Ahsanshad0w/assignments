operator= input("Choose operator (+, -, /, *, power): ")
firstval= int(input("Input first value: "))
secondval= int(input("Input second value: "))
result=0
if operator=='+':
    result= firstval+ secondval
elif operator=='-':
    result= firstval- secondval
elif operator== '*':
    result= firstval* secondval
elif operator== 'power':
    result= firstval**secondval

print(f"The Result of {firstval} {operator} {secondval} is : {result} ")