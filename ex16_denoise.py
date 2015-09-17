import re

filename = 'baladhuri_futuh.txt'
text = open(filename, mode='r', encoding='utf-8').read()

denoised_text = re.sub(r"َ|ً|ُ|ٌ|ِ|ٍ|ْ|ّ|ـ", "", text)

print(text[:500])
print(denoised_text[:500])
