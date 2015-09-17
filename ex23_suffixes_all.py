import re

filename = 'baladhuri_futuh.txt'
text = open(filename, mode='r', encoding='utf-8').read()

def word_counter(search_word, search_text): 
    freq_word = len(re.findall(search_word, search_text))
    freq_word = str(freq_word)
    print(search_word + ' appears ' + freq_word + ' times in this text')


word = r"\bحكمي?(?:ت|ا|ي|و|ات|ن|تم|تمو|تما|تن|تا|نا|وا)?ن?(?:ة|ى|ني|ي|نا|ك|كم|كما|كن|ه|ها|هم|هن|هما|ن)?\b"
word_counter(word, text)

