num = int(input())
if num > 0:
    print("Положительное")
elif num < 0:
    print("Отрицательное")
else:
    print("Ноль")
if 10 <= num <= 50:
    print("Число входит в диапазон [10, 50]")
else:
    print("Число не входит в диапазон [10, 50]")