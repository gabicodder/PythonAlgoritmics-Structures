import random
import string

def run():
    print('\n\t******:::::::Password Generator::::::*******\n')
    password = []
    for i in range(8):
        password.append(random.choice(string.ascii_letters))
        password.append(str(random.randint(1,11)))
        password.append(random.choice(string.punctuation))   
    password = "".join(password)
    print(f'Tu password es: {password}')

if __name__ == "__main__":
    run()
