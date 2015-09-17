import re

filename = 'baladhuri_futuh.txt'
text = open(filename, mode='r', encoding='utf-8').read()

list_of_words = re.findall('\w+', text)

unique_words = set(list_of_words)
print(len(unique_words))
