def clear_names(file_name: str) -> list:
    """Функция для очистки имён от лишних символов"""
    new_names_list = list()
    with open(r'C:/Users/user/PycharmProjects/pythonProject9.2/data/names.txt' ) as names_file:
        names_list = names_file.read().split()
        for name_item in names_list:
            new_name = ''
            for symbol in name_item:
                if symbol.isalpha():
                    new_name += symbol
            if new_name.isalpha():
                new_names_list.append(new_name)
    return new_names_list

print(clear_names(r'C:\Users\user\PycharmProjects\pythonProject9.2\data\names.txt'))

# if __name__ == '__main__':
#     cleared_name = clear_names(r'C:\Users\user\PycharmProjects\pythonProject9.2\data\names.txt')
#
#     for i in cleared_name:
#         print(i)
# изменения