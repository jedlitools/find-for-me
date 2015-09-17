import re

filename = 'tabari_tarikh.txt'
text = open(filename, mode='r', encoding='utf-8').read()

search_results = re.findall("[أإآٱا]صغر", text)

print(len(search_results))
