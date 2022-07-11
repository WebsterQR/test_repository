import backend

print("Что хотите сделать? 1 - сложение, 2 - умножение, 3 - вычитание, 4 - деление")
d = int(input())
a = int(input("Введите первое число"))
b = int(input("Введите число"))

print(backend.result(a, b, d))