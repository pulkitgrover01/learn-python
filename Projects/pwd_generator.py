import random
import string

def password_generator(length = 10):
    random_password = string.digits + string.ascii_letters + string.punctuation
    return "".join(random.choice(random_password) for _ in range(length))


print(password_generator(4)) 



