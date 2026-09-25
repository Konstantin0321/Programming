from collections import Counter

text = input("Введите строку: ").lower()
counter = Counter(text)
top_3 = counter.most_common(3)

print("3 самых частых символа:")
for symbol, count in top_3:
    print(symbol, "-", count)