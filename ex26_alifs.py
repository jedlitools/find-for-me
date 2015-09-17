import re

filename = 'tabari_tarikh.txt'
text = open(filename, mode='r', encoding='utf-8').read()

modified_text = re.sub("أ|إ|آ|ٱ", "ا", text)

search_results = re.findall("اصغر", modified_text)

print(len(search_results))
