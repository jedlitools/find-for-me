import re

text = open('khalifa_tarikh.txt', mode="r", encoding="utf-8").read()
text = re.sub(r"َ|ً|ُ|ٌ|ِ|ٍ|ْ|ّ|ـ", "", text)

def search_words(checklist):
    search_words = open(checklist, mode='r', encoding='utf-8').read().splitlines()
    return search_words

def index_generator(word, text):
    juz = 'الجزء:'
    safha = 'الصفحة:'
    page_regex = juz + r' \d+ ¦ ' + safha + r' \d+'
    search_regex = word + r'.+?(' + page_regex + ')'
    pagination = re.findall(search_regex, text, re.DOTALL)
    return pagination

region = r"[وفبل]{0,2}"+r"[اأإآ]" +"فريقي" +r"[اةه]"

def context_search(region, checklist):
    gov_words = search_words(checklist)
    regex = "(?:\S+\s+){0,8}"+region+"(?:\s+\S+){0,8}"
    contexts = re.findall(regex, text, re.DOTALL)
    outcomes = []
    for passage in contexts:
        for word in gov_words:
            pre_all = r"(?:و|ف|ب|ل|ك|ال|أ|س|ت|ي|ن|ا){0,6}"
            su_all = r"(?:و|ن|ه|ى|ا|تما|ها|نا|ت|تم|هم|كم|ة|كما|تمو|كن|هما|ي|وا|ني|ات|هن|تن|ك|تا){0,4}"
            regex_w = r"\b" + pre_all + word + su_all + r"\b"
            if len(re.findall(regex_w, passage)) > 0:
                passage_page = index_generator(passage, text)
                passage = re.sub(r"\n", " ", passage)
                outcomes.append((passage, passage_page))
                break
    return outcomes

governors = context_search(region, 'governors_checklist.txt')

e=1
for s, p in governors:
    print(e, "\n", s, "\n", p, "\n\n")
    e = e+1
