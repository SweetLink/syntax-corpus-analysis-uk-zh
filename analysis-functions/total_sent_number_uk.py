# import spacy

# # Завантаження моделі для української мови
# nlp = spacy.load("uk_core_news_sm")
# nlp.max_length = 2000000

# def count_sentences(filename):
#     # Відкриття файлу і читання його вмісту
#     with open(filename, 'r', encoding='utf-8') as file:
#         text = file.read()
    
#     # Парсинг тексту за допомогою spaCy
#     doc = nlp(text)
    
#     # Підрахунок кількості речень
#     sentence_count = len(list(doc.sents))
    
#     return sentence_count

# # Шлях до файлу з корпусом
# filename = "uk-zh.txt (1)/TED2020.uk-zh.uk"

# # Отримання кількості речень у файлі
# total_sentences = count_sentences(filename)

# print("Загальна кількість речень у корпусі:", total_sentences)

#Загальна кількість речень у корпусі: 13861



import spacy

def count_sentences(filename):
    nlp = spacy.load("uk_core_news_sm")
    nlp.max_length = 2000000
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    doc = nlp(text)
    return len(list(doc.sents))

filename = "uk-zh.txt (1)/TED2020.uk-zh.uk"

total_sentences = count_sentences(filename)
print("Total number of sentences in the corpus:", total_sentences)

#Загальна кількість речень у корпусі: 13861