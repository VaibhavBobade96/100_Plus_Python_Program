num1 = int(input("please enter a number1 ="));
num2 = int(input("Please enter a number2 ="));

op = input("please select the operator (+, - , /, *) : ");

if op == '+':
    print("addition of a and b :", num1 + num2);

elif op == '-':
    print("Substraciton of a and b :", num1 - num2);

elif op == '/' :
    if num2 != 0:
        print("substraction of a and b :", num1 / num2);
    else :
        print("Not Divided by zero");

elif op == '*' :
    print("Multiplication of a and b :", num1 * num2);


else:
    print("invalid Operator");




