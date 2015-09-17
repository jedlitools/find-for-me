import re

filename = 'baladhuri_futuh.txt'
text = open(filename, mode='r', encoding='utf-8').read()

results  = re.findall('البصرة', text)
print(len(results))
