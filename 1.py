import random
import string

a = int(input(“Введи число для довжини ”))

def generate_password(length=a):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for i in range(a))
