def chaicoder(num):
    def actual(x):
        return x**num
    return actual
f=chaicoder(2)
g=chaicoder(3)
print(f(2))
print(g(3))
