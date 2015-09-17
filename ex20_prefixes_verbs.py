import re

filename = 'baladhuri_futuh.txt'
text = open(filename, mode='r', encoding='utf-8').read()

def word_counter(search_word, search_text): 
    freq_word = len(re.findall(search_word, search_text))
    freq_word = str(freq_word)
    print(search_word + ' appears ' + freq_word + ' times in this text')


word = r"\b(?:و|ف)?(?:أ|ت|ي|ن|ا)?حكم(?:)\b"
word_counter(word, text)

