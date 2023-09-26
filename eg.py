#Tip Calculator

bill = str(input("Bill: "))
tip = int(input("Tip: "))

float(bill)
total_amount_paid = print(bill) + print(tip)

ge=("great")
bad=("bad")
oka=("okay")
go=("good")


x=input("Service:")



if x == ge:
    total = bill * 1.25
elif x == bad:
    total = bill * 1.00
elif x == oka:
    total = bill * 1.15
elif x == go:
    total = bill * 1.20


print(f"${total}")

