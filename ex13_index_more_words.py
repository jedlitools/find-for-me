import re

filename = 'baladhuri_futuh.txt'
text = open(filename, mode='r', encoding='utf-8').read()

def index_generator(word, text):
    juz = 'الجزء:'
    safha = 'الصفحة:'
    page_regex = juz + r' \d+ ¦ ' + safha + r' \d+'
    search_regex = word + r'.+?(' + page_regex + ')'
    pagination = re.findall(search_regex, text, re.DOTALL)
    return pagination

search_words = ['عيسابا']
for word in search_words: 
    index = index_generator(word, text)
    print(word)
    for page in index:
        print(page)

