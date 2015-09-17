import re

filename = 'baladhuri_futuh.txt'
text = open(filename, mode='r', encoding='utf-8').read()

word = 'فرضة'
word_instances = re.findall(word, text)
freq_word = len(word_instances)
freq_word = str(freq_word)
print(word + ' appears ' + freq_word + ' times in this text')
