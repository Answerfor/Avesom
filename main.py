import re

# Путь к файлу с данными
input_file = "names.txt"
output_file = "filtered_names.txt"

# Функция для проверки, состоит ли слово только из двух частей (имя и фамилия)
def is_two_parts(word):
    # Проверяем, чтобы в слове было только два слова (буквенные части) без цифр
    return len(re.findall(r'[a-zA-Z]+', word)) == 2 and not re.search(r'\d', word)

# Читаем файл и фильтруем строки
with open(input_file, 'r') as file:
    data = file.read().splitlines()

# Отбираем только те слова, которые состоят из двух частей
filtered_words = [word for word in data if is_two_parts(word)]

# Записываем результат в новый файл
with open(output_file, 'w') as file:
    file.write('\n'.join(filtered_words))

print(f"Фильтрованные слова сохранены в файл {output_file}.")
