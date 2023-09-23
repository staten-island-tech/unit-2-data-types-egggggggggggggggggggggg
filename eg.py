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
if x == bad:
    total = bill * 1.00
if x == oka:
    total = bill * 1.15
if x == go:
    total = bill * 1.20


print(f"${total}")

