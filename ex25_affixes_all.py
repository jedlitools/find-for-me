import re

filename = 'baladhuri_futuh.txt'
text = open(filename, mode='r', encoding='utf-8').read()

def word_counter(search_word, search_text): 
    freq_word = len(re.findall(search_word, search_text))
    freq_word = str(freq_word)
    print(search_word + ' appears ' + freq_word + ' times in this text')


pre_all = r"(?:و|ف|ب|ل|ك|ال|أ|س|ت|ي|ن|ا){0,6}"
su_all = r"(?:و|ن|ه|ى|ا|تما|ها|نا|ت|تم|هم|كم|ة|كما|تمو|كن|هما|ي|وا|ني|ات|هن|تن|ك|تا){0,4}"
search_regex = r"\b"+pre_all+"حكم"+su_all+r"\b"

word_counter(search_regex, text)

