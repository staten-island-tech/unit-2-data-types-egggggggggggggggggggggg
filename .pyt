 
#FACTORING MACHINE


num = int(input("NUMBER : "))


    

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


x = input("Southbound? ")
y = input("Westbound? ")

def traffic(x, y):
    if x == y:
          print("false")
    else:
          print("true")

traffic(x,y) 


