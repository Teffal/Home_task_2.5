
# заготовка для домашней работы
# прочитайте про glob.glob
# https://docs.python.org/3/library/glob.html

# Задание
# мне нужно отыскать файл среди десятков других я знаю некоторые части этого файла
# (на память или из другого источника) я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно выводит количество найденных файлов
# 2. снова ожидает ввод поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции
# на зачёт с отличием, использовать папку 'Advanced Migrations'

import glob
import os.path
import re
from pprint import pprint

migrations = 'Migrations'
files = glob.glob(os.path.join(migrations, "*.sql"))

def search_word_in_files(files, search_string):
	new_list_files = []
	for file in files:
		with open(file) as f:
			for line in f:
				if not len(line.strip()):
					continue
				if re.search(search_string.lower(), line.strip().lower()):
					new_list_files.append(file)
					break
	pprint(new_list_files)
	print(len(new_list_files))
	return new_list_files

def main():
	migrations = input('Enter directory: ')
	if not migrations: files = glob.glob(os.path.join('Migrations', "*.sql"))
	else: files = glob.glob(os.path.join(migrations, "*.sql"))

	while True:
		search_string = input('Please enter your string: (if you will want to exit from the program, enter "q" )')
		if search_string == 'q' or search_string == '': exit()
		files = search_word_in_files(files, search_string)

main()