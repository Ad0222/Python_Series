age=6
day="wednesday"
# price=12 if age>=18 else 8
if age>=18:
    price=12
else:
    price=8
print(price)

if day=="wednesday":
    price-=2
    print("Discount $",price)
