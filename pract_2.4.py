def f(n):
    if n == 1:
        return 1
    return f(n-1) * n

a = int(input("введите число\n"))
if a < 0:
    print("число должно быть больше 0")
    exit()
if a == 0:
    print("число не должно быть ровно нулю")
    exit()

print("факториал который вы ввели равен ", f(a))