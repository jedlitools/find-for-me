import re

filename = 'baladhuri_futuh.txt'
text = open(filename, mode='r', encoding='utf-8').read()

def word_counter(search_word, search_text): 
    freq_word = len(re.findall(search_word, search_text))
    freq_word = str(freq_word)
    print(search_word + ' appears ' + freq_word + ' times in this text')


word = r"\bحكم(?:و|ن|ه|ى|ا|تما|ها|نا|ت|تم|هم|كم|ة|كما|تمو|كن|هما|ي|وا|ني|ات|هن|تن|ك|تا){0,4}\b"
word_counter(word, text)

