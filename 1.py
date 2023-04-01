from typing import Dict


def generate_vigenere_key(keyword: str) -> Dict[int, int]:
    """
    Генерирует ключ шифрования для шифра Виженера с заданным ключевым словом.

    :param keyword: Ключевое слово для генерации ключа.
    :return: Ключ шифрования в виде словаря, где индексу символа исходного текста соответствует значение сдвига.
    """
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    return {index: (ord(keyword_char) - ord("А")) for index, keyword_char in enumerate(keyword)}


def vigenere_cipher(text: str, keyword: str, encrypt=True) -> str:
    """
    Шифрует или дешифрует текст с использованием заданного ключевого слова шифра Виженера.

    :param text: Исходный текст для шифрования или зашифрованный текст для дешифрования.
    :param keyword: Ключевое слово для шифра Виженера.
    :param encrypt: Если True, выполняется шифрование, иначе - дешифрование.
    :return: Зашифрованный или дешифрованный текст.
    """
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    result = []
    keyword_index = 0
    for char in text:
        if char.upper() in alphabet:
            shift = ord(keyword[keyword_index % len(keyword)]) - ord("А")
            if not encrypt:
                shift = -shift
            new_index = (alphabet.index(char.upper()) + shift) % len(alphabet)
            result.append(alphabet[new_index] if char.isupper() else alphabet[new_index].lower())
            keyword_index += 1
        else:
            result.append(char)
    return "".join(result)


KEYWORD = "ИБАС"  # Укажите ключевое слово для шифра Виженера

ORIGINAL_TEXT = "На краю дороги стоял дуб. Вероятно, в десять раз старше берез, составлявших лес, он был в десять раз " \
                "толще, и в два раза выше каждой березы. Это был огромный, в два обхвата дуб, с обломанными, давно, " \
                "видно, суками и с обломанной корой, заросшей старыми болячками. С огромными своими неуклюже, " \
                "несимметрично растопыренными корявыми руками и пальцами, он старым, сердитым и презрительным уродом " \
                "стоял между улыбающимися березами. Только он один не хотел подчиняться обаянию весны и не хотел " \
                "видеть ни весны, ни солнца. Весна, и любовь, и счастие! — как будто говорил этот дуб. — И как не " \
                "надоест вам все один и тот же глупый бессмысленный обман! Все одно и то же, и все обман! Нет ни " \
                "весны, ни солнца, ни счастья. Вон смотрите, сидят задавленные мертвые ели, всегда одинакие, " \
                "и вон и я растопырил свои обломанные, ободранные пальцы, где ни выросли они — из спины, " \
                "из боков. Как выросли — так и стою, и не верю вашим надеждам и обманам»."

if __name__ == "__main__":
    key = generate_vigenere_key(KEYWORD)
    encrypted_text = vigenere_cipher(ORIGINAL_TEXT, KEYWORD, encrypt=True)
    decrypted_text = vigenere_cipher(encrypted_text, KEYWORD, encrypt=False)

    print(f"Исходный текст: {ORIGINAL_TEXT}")
    print(f"Зашифрованный текст: {encrypted_text}")
    print(f"Дешифрованный текст: {decrypted_text}")

    # Запись в файл encrypted_text.txt
    with open("1. encrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(encrypted_text)

    # Запись в файл decrypted_text.txt
    with open("1. decrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(decrypted_text)

    # Запись в файл key.txt
    with open("1. key.txt", "w", encoding="utf-8") as f:
        f.write(str(key))
