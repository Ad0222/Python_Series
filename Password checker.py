password=len("123456")

if password<=6:
    print("weak")
elif password<=10:
    print("medium")
else:
    print("strong")