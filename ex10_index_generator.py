import re

filename = 'baladhuri_futuh.txt'
text = open(filename, mode='r', encoding='utf-8').read()

juz = 'الجزء:'
safha = 'الصفحة:'

page_regex = juz + r' \d+ ¦ ' + safha + r' \d+'

print(re.findall(page_regex, text))
