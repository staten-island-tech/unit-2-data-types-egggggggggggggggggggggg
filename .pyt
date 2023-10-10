


#GCF
num = int(input("NUMBER 1: "))
num2 = int(input("NUMBER 2 : "))

def gcf(x, y):
    while y:
      x, y = y, x % y
    return x

print(f"The Greatest Common Factor of {num} and {num2} is " + str(gcf(num, num2)))
