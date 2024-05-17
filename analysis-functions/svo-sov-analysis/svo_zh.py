# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.tag import pos_tag

import spacy

# Завантаження моделей мови
nlp_zh = spacy.load("zh_core_web_sm")

def count_svo_sentences(text, nlp):
    doc = nlp(text)
    svo_count = 0
    for sent in doc.sents:
        has_s = False
        has_v = False
        has_o = False
        for token in sent:
            if token.dep_ == "nsubj" and token.pos_ == "NOUN":
                has_s = True
            elif token.dep_ == "dobj" and token.pos_ == "NOUN":
                has_o = True
            elif token.pos_ == "VERB":
                has_v = True
        if has_s and has_v and has_o:
            svo_count += 1
    return svo_count

# Завантаження українського корпусу
# with open('uk-zh.txt (1)/TED2020.uk-zh.uk', 'r', encoding='utf-8') as file:
#     ukr_corpus = file.read()

# svo_count_ukr = 0
chunk_size = 100000  # Розмір кожного шматка тексту для обробки
# for i in range(0, len(ukr_corpus), chunk_size):
#     chunk = ukr_corpus[i:i+chunk_size]
#     svo_count_ukr += count_svo_sentences(chunk, nlp_uk)
# print("Кількість речень українською мовою зі схемою SVO:", svo_count_ukr)

# Завантаження китайського корпусу
with open('uk-zh.txt (1)/TED2020.uk-zh.zh', 'r', encoding='utf-8') as file:
    chinese_corpus = file.read()

svo_count_chinese = 0
for i in range(0, len(chinese_corpus), chunk_size):
    chunk = chinese_corpus[i:i+chunk_size]
    svo_count_chinese += count_svo_sentences(chunk, nlp_zh)
print("Кількість речень китайською мовою зі схемою SVO:", svo_count_chinese)



#Працює для кит SVO
#Кількість речень китайською мовою зі схемою SVO: 2058


