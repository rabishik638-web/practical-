from arithmetic import add, sub, mul

a = int(input("Enter the A value: "))
b = int(input("Enter the B value: "))

print("Addition of", a, "and", b, "value is:", add(a, b))
print("Subtraction of", a, "and", b, "value is:", sub(a, b))
print("Multiplication of", a, "and", b, "value is:", mul(a, b))