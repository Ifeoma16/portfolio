import random
import string

length = int(input('Enter the length of your desired password : '))

all = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.sample(all, length))
print(password)