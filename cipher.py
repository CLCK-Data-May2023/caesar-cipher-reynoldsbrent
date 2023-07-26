user_sentence = input("Please enter a sentence: ")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
encrypted_string = ""
for letter in user_sentence.lower():
    if letter in alphabet:
        if alphabet.index(letter) <= 20:
            new_letter = alphabet[alphabet.index(letter) + 5]
            encrypted_string += new_letter
        else:
            new_letter = alphabet[4 - (25 - alphabet.index(letter))]
            encrypted_string += new_letter
    else:
        encrypted_string += letter

print("The encrypted sentence is: " + encrypted_string)
