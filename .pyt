 
#FACTORING MACHINE


num = int(input("NUMBER : "))
num2 = int(input("NUMBER 2 : "))

    

def factor(x): 
    print("Factors of ",x," : ")
    for i in range(1, x + 1): 
        if x % i == 0 : 
            print(i) 




factor(num)

#ODD?EVEN

num1=int(input("Number: "))


def eo(x):
    if (num1 % 2) == 0: 
        print("even")
    else : print("odd")

eo(num1)