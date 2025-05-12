# number=int(input("given a number:"))

# for i in range(1,number+1):
#     if i>0:
#        print(i)

while True:
    number=int(input("given 1 to 10 between"))
    if 1<=number<=10:
        print("Thanks")
        break
    else:
        print("invalid number")