
def palindrome2(word):
    reverse_word = word[::-1]

    if reverse_word == word:
        return True
    
    return False
    
def palindrome(word):
    reversed_letters = []
    
    for letter in word:
        reversed_letters.insert(0, letter)
        
    reversed_word = ''.join(reversed_letters)
    
    if reversed_word == word:
        return True
    
    return False

if __name__ == "__main__":
    word = str(input("Write a word: "))
    
    result = palindrome2(word)
    
    if result is True:
        print("{} it is a palindrome".format(word))
    else:
        print("{} it is not a palindrome".format(word))