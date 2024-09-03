import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Adivinhe o número entre 1 e {x}: "))
        if guess < random_number:
            print("Errou! Tente de novo, foi muito baixo.")
        elif guess > random_number:
            print("Errou! Número muito alto, tente de novo.")
        
    print(f"Você adivinhou o número {random_number} corretamente!")

guess(20)