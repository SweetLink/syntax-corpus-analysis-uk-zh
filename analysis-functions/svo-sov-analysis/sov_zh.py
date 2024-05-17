import spacy

# Завантаження моделі для китайської мови
nlp = spacy.load("zh_core_web_sm")

# Функція для визначення структури речення SOV
def find_sov_sentences(text):
    sov_sentences = []
    doc = nlp(text)
    for sentence in doc.sents:
        for token in sentence:
            if token.dep_ == 'nsubj' and token.head.dep_ == 'dobj' and token.head.head.pos_ == 'VERB':
                sov_sentences.append(sentence.text)
                break
    return sov_sentences

# Завантаження корпусу китайської мови
with open('corpus-uk-zh/TED2020.uk-zh.zh', 'r', encoding='utf-8') as file:
    corpus = file.read()

sov_sentences = find_sov_sentences(corpus)

# Підрахунок кількості речень за схемою SOV
sov_count = len(sov_sentences)

print("Кількість речень зі схемою SOV у корпусі:", sov_count)

#Працює для кит схеми
#Кількість речень зі схемою SOV у корпусі: 251