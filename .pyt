num = int(input("NUMBER : "))
num2 = int(input("NUMBER 2 : "))

def factor(x):
    print("The factors of ",x," are")
    for i in range(1, x + 1 ):
        if x % i == 0 : 
            print(i)

def gcf(a, b): 
    if (a == 0): 
        return b
    else:
        return gcf(a, a % b)

print("The GCF of ",num," and ",num2," is : ")
print(gcf(num, num2))