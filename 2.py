import json


def read_key_from_file(_filename: str) -> dict:
    """
    Читает ключ из файла формата json и возвращает его в виде словаря

    :param _filename: имя файла
    :return: словарь с ключом
    """
    with open(_filename, 'r', encoding='utf-8') as _file:
        _key = json.load(_file)
    return _key


def decrypt_text(text: str, _key: dict) -> str:
    """
    Дешифрует текст по ключу и возвращает дешифрованный текст

    :param text: Зашифрованный текст
    :param _key: Ключ для дешифровки
    :return: Дешифрованный текст
    """
    deciphered_text = ""
    for char in text:
        if char in _key:
            deciphered_text += _key[char]
        else:
            deciphered_text += char
    return deciphered_text


if __name__ == '__main__':
    filename = "2. key.json"
    with open("2. cod2.txt", 'r', encoding='utf-8') as file:
        ciphered_text = file.read()

    key = read_key_from_file(filename)
    decrypted_text = decrypt_text(ciphered_text, key)

    with open("2. decrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(decrypted_text)

    print("Дешифрованный текст:", decrypted_text)
