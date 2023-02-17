SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def read_file() -> str:
    with open("task_1_decryption.txt", "r", encoding='utf-8') as file:
        return file.read()


def check_key(key: str) -> bool:
    for sym in SYMBOLS:
        if(key.count(sym) != 1):
            return False
    return True


if "__main__" == __name__:
    
    key = input("Введите ключ: ").lower()
    if(len(key) != 33 and not check_key(key)):
        print("Вы неправильно ввели ключ!")
        exit(0)

    text = read_file().lower()

    for i, sym in enumerate(SYMBOLS):
        text = text.replace(sym, key[i])

    with open("task_1_encryption.txt", "w", encoding='utf-8') as file:
        file.write(text)