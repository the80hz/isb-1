from task_1 import read_file, write_file


def unique_sym(chiphertext: str) -> list:
    '''displays information about the number and frequency of occurrence of unique characters'''
    list_sym = list()

    for sym in chiphertext:
        if(sym not in list_sym):
            list_sym.append(sym)
            count_sym = chiphertext.count(sym)
            print(sym, count_sym, count_sym / len(chiphertext), sep="   ")


if "__main__" == __name__:
    chiphertext = read_file("task_2_encryption.txt")
    unique_sym(chiphertext)

    chiphertext = chiphertext.replace(" ", "р")
    chiphertext = chiphertext.replace("2", " ")
    chiphertext = chiphertext.replace("Я", "п")
    chiphertext = chiphertext.replace(">", "с")
    chiphertext = chiphertext.replace("К", "е")
    chiphertext = chiphertext.replace("Ь", "о")
    chiphertext = chiphertext.replace("9", "ц")
    chiphertext = chiphertext.replace("r", "в")
    chiphertext = chiphertext.replace("<", "м")
    chiphertext = chiphertext.replace("Ы", "н")
    chiphertext = chiphertext.replace("t", "и")
    chiphertext = chiphertext.replace("О", "т")
    chiphertext = chiphertext.replace("Ч", "л")
    chiphertext = chiphertext.replace("Д", "а")
    chiphertext = chiphertext.replace("М", "з")
    chiphertext = chiphertext.replace("1", "я")
    chiphertext = chiphertext.replace("Х", "ю")
    chiphertext = chiphertext.replace("8", "ы")
    chiphertext = chiphertext.replace("Е", "б")
    chiphertext = chiphertext.replace("0", "у")
    chiphertext = chiphertext.replace("Л", "ж")
    chiphertext = chiphertext.replace("Й", "к")
    chiphertext = chiphertext.replace("a", "ч")
    chiphertext = chiphertext.replace("Б", "д")
    chiphertext = chiphertext.replace("c", "щ")
    chiphertext = chiphertext.replace("Ф", "э")
    chiphertext = chiphertext.replace(".", "ф")
    chiphertext = chiphertext.replace("А", "г")
    chiphertext = chiphertext.replace("Б", "д")
    chiphertext = chiphertext.replace(",", "ь")
    chiphertext = chiphertext.replace("b", "ш")
    chiphertext = chiphertext.replace("3", "х")
    
    write_file("task_2_decryption.txt", chiphertext)