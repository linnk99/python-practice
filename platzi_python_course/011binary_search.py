import random

def generate_list(numbers):
    for i in range(0, random.randrange(0, 100)):
        numbers.append(random.randint(0, 1000))
    
    numbers.sort()            

def binary_search(numbers, number_to_find, low, high):
    if low > high:
        return False
    
    mid = (low + high) // 2
    
    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    else:
        return binary_search(numbers, number_to_find, mid + 1, high)

if __name__ == "__main__":
    numbers = []
    generate_list(numbers)
    
    print(numbers)
    
    number_to_find = int(input("Ingresa un número: "))
    
    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)
    
    if result is True:
        print("El número si está en la lista ")
    else:
        print("El número no está en la lista")