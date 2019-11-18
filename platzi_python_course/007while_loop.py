import random

def run():
    number_found = False
    random_number = random.randint(0,20)
    
    while not number_found:
        number = int(input("Intenta un numero: "))
        
        if number == random_number:
            print("Felicidades, encontraste el numero secreto")
            number_found = True
        elif number > random_number:
            print("El numero secreto es menor")
        elif number < random_number:
            print("El numero secreto es mayor")
    
if __name__ == "__main__":
    run()