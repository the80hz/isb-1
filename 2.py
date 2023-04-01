import json


def read_key_from_file(filename: str) -> dict:
    with open(filename, 'r', encoding='utf-8') as file:
        key = json.load(file)
    return key


def decrypt_text(text: str, key: dict) -> str:
    deciphered_text = ""
    for char in text:
        if char in key:
            deciphered_text += key[char]
        else:
            deciphered_text += char
    return deciphered_text


filename = "2. key.json"
with open("2. cod2.txt", 'r', encoding='utf-8') as file:
    ciphered_text = file.read()

key = read_key_from_file(filename)
decrypted_text = decrypt_text(ciphered_text, key)

with open("2. decrypted_text.txt", "w", encoding="utf-8") as f:
    f.write(decrypted_text)

print("Дешифрованный текст:", decrypted_text)
