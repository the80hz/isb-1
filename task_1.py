SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def read_file(filename: str) -> str:
    '''return text from read file'''
    with open(filename, "r", encoding='utf-8') as file:
        return file.read()


def write_file(filename: str, text: str) -> None:
    '''Writing ciphertext to a text file'''
    with open(filename, "w", encoding='utf-8') as file:
        file.write(text)


def check_key(key: str) -> bool:
    '''Checking a key for duplicate or missing characters'''
    for sym in SYMBOLS:
        if(key.count(sym) != 1):
            return False
    return True


if "__main__" == __name__:
    key = input("Enter the key: ").lower()
    if(len(key) != 33 and not check_key(key)):
        print("You entered the key incorrectly!")
        exit(0)

    text = read_file("task_1_decryption.txt").lower()

    for i, sym in enumerate(SYMBOLS):
        text = text.replace(sym, key[i])

    write_file("task_1_encryption.txt", text)