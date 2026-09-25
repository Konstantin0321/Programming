import random
import string

letters = random.choices(string.ascii_uppercase, k=3)
digits = random.choices(string.digits, k=3)
symbols = random.choices("!@#$%^&*", k=2)
password = letters + digits + symbols
random.shuffle(password)
password = "".join(password)

print(password)