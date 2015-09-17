import re

filename = 'baladhuri_futuh.txt'
text = open(filename, mode='r', encoding='utf-8').read()

list_of_words = re.findall(r'\w+', text)
print(list_of_words[:50])


