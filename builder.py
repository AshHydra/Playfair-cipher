def prepare_text(text):
    # Odstranit mezery, převést na velká písmena a nahradit "J" písmenem "I"
    text = text.replace(" ", "").upper().replace("J", "I")
    # Doplň doplňující znak, pokud je délka lichá
    if len(text) % 2 != 0:
        text += "X"
    print(text)
    return text

def valid_key(key):
    string = ""
    key = key.upper()
    for letter in key:
        if (letter not in string):
            string = string + letter
        else:
            return False
    return True


def build_playfair_matrix(key):
    # Vytvoření prázdné matice 5x5
    matrix = [['' for _ in range(5)] for _ in range(5)]
    used_letters = set()
    key = prepare_text(key)

    row, col = 0, 0

    # Naplnění matice klíčovým slovem
    for letter in key:
        if letter not in used_letters:
            matrix[row][col] = letter
            used_letters.add(letter)
            col += 1
            if col == 5:
                col = 0
                row += 1

    # Přidání zbývajících písmen (kromě J) do matice
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if letter != 'J' and letter not in used_letters:
            matrix[row][col] = letter
            used_letters.add(letter)
            col += 1
            if col == 5:
                col = 0
                row += 1

    return matrix

def playfair_encrypt(plaintext, key):
    plaintext = prepare_text(plaintext)
    matrix = build_playfair_matrix(key)
    encrypted_text = []
    filtered_text = ""

    # Šifrování dvojic písmen
    for i in range(0, len(plaintext), 2):
        letter1 = plaintext[i]
        letter2 = plaintext[i + 1]

        # Pokud jsou písmena ve stejných dvojicích stejná, vložit 'X' mezi ně
        if letter1 == letter2:
            letter2 = 'X'
            

        filtered_text = filtered_text +letter1 + letter2 +" "

        # Najdi pozice písmen v matici
        row1, col1 = None, None
        row2, col2 = None, None

        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter1:
                    row1, col1 = row, col
                if matrix[row][col] == letter2:
                    row2, col2 = row, col

        # Aplikace pravidel pro šifrování
        if row1 == row2:  # Písmena jsou ve stejném řádku
            encrypted_text.append(matrix[row1][(col1 + 1) % 5])
            encrypted_text.append(matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:  # Písmena jsou ve stejném sloupci
            encrypted_text.append(matrix[(row1 + 1) % 5][col1])
            encrypted_text.append(matrix[(row2 + 1) % 5][col2])
        else:  # Písmena jsou ve různých řádcích a sloupcích
            encrypted_text.append(matrix[row1][col2])
            encrypted_text.append(matrix[row2][col1])
    
    print(filtered_text)
    return ''.join(encrypted_text)

def playfair_decrypt(ciphertext, key):
    ciphertext = prepare_text(ciphertext)
    matrix = build_playfair_matrix(key)
    decrypted_text = []

    # Dešifrování dvojic písmen
    for i in range(0, len(ciphertext), 2):
        letter1 = ciphertext[i]
        letter2 = ciphertext[i + 1]

        # Najdi pozice písmen v matici
        row1, col1 = None, None
        row2, col2 = None, None

        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter1:
                    row1, col1 = row, col
                if matrix[row][col] == letter2:
                    row2, col2 = row, col

        # Aplikace pravidel pro dešifrování
        if row1 == row2:  # Písmena jsou ve stejném řádku
            decrypted_text.append(matrix[row1][(col1 - 1) % 5])
            decrypted_text.append(matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:  # Písmena jsou ve stejném sloupci
            decrypted_text.append(matrix[(row1 - 1) % 5][col1])
            decrypted_text.append(matrix[(row2 - 1) % 5][col2])
        else:  # Písmena jsou ve různých řádcích a sloupcích
            decrypted_text.append(matrix[row1][col2])
            decrypted_text.append(matrix[row2][col1])

    return ''.join(decrypted_text)

# Hlavní část programu
if __name__ == '__main__':
    key = input("Zadejte klíčové slovo: ")
    if(valid_key(key)):
        
        plaintext = input("Zadejte text k zašifrování: ")

        encrypted_text = playfair_encrypt(plaintext, key)
        print(f"Zašifrovaný text: {encrypted_text}")

        decrypted_text = playfair_decrypt(encrypted_text, key)
        print(f"Odšifrovaný text: {decrypted_text}")
    else:
        print("not a valid key")
        