# First program:-
# username="chaiaurcode"
# def func(username):
#     # username="chai"
#     return username
# print(func(username))

# Second program
# x=99
# def f(y):
#     z=x+y
#     return z
# result=f(1)
# print(result)

# Third program
# x=99
# def f1():
#     x=88
#     print(x)
#     # def f2():
#     #     print(x)
#     # f2()
# f1()

# Fourth program
# x=99
# def f():
#     global x
#     x=12
# f()
# print(x)

#Five program
x=99
def f():
    x=88
    def f1():
        print(x)
    return f1
myresult=f()
myresult()
        