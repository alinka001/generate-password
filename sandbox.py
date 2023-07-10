import random


def file_reader() -> list[str]:
    try:
        file = open('input.txt', 'r')
        words_list = []
        for line in file:
            if len(line) > 3:
                words_list.append(line[0:-1])
            else:
                continue
        file.close()
        return words_list
    except FileNotFoundError:
        print("Файл не найден")
        
    


def random_index(options_list: list[str]) -> int:
    try:
        highest_index = len(options_list) - 1
        return random.randint(0, highest_index)
    except TypeError :
        pass



if __name__ == "__main__":
    try:
        while True :
            words_list = file_reader()
            random_index_1 = random_index(words_list)
            random_index_2 = random_index(words_list)
            password = words_list[random_index_1].title() + words_list[random_index_2].title()
            if 7 < len(password) < 10 :
                print(password)
                break
    except TypeError:
        print("Error")
    