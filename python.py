#GCF




#Tips
total = int(input("Total? "))
service = str(input("Rate the Service? "))

ge = ("great")
go = ("good")
bad = ("bad")
norm = ("normal")

def tipcalc(x, y): 
   if x == go: 
      total = y * 1.15 
   if x == ge: 
      total = y * 1.25
   if x == norm: 
      total = y * 1.20
   if x == bad: 
     total =  y * 1
print(total)

  
  
  
  
tipcalc(service , total)

