# import spacy

# def count_subordinate_clauses(text):
#     nlp = spacy.load("uk_core_news_sm")
#     subordinate_clause_count = 0
#     for chunk in split_text_into_chunks(text, chunk_size=50000):  # Split into chunks of 50,000 characters
#         doc = nlp(chunk)
#         for sentence in doc.sents:
#             for token in sentence:
#                 if token.dep_ == "ccomp":
#                     subordinate_clause_count += 1
#     return subordinate_clause_count

# def split_text_into_chunks(text, chunk_size):
#     chunks = []
#     for i in range(0, len(text), chunk_size):
#         chunks.append(text[i:i + chunk_size])
#     return chunks

# # Read the corpus from the file
# with open('uk-zh.txt (1)/TED2020.uk-zh.uk', 'r', encoding='utf-8') as file:
#     corpus = file.read()

# subordinate_clauses = count_subordinate_clauses(corpus)
# print("Кількість складнопідрядних речень в корпусі:", subordinate_clauses)

#Кількість складнопідрядних речень в корпусі: 2161

import spacy

# Завантажуємо модель для української мови
nlp = spacy.load("uk_core_news_sm")

def count_subordinate_clauses(text):
    doc = nlp(text)
    subordinate_count = 0

    for sent in doc.sents:
        # Перевіряємо, чи є поточне речення складнопідрядним
        if any(token.dep_ == 'advcl' or token.dep_ == 'acl' for token in sent):
            subordinate_count += 1

    return subordinate_count

# Зчитуємо текст з файлу
with open("uk-zh.txt (1)/TED2020.uk-zh.uk", "r", encoding="utf-8") as file:
    text = file.read()

# Розділяємо текст на менші частини (по 500000 символів)
text_parts = [text[i:i+500000] for i in range(0, len(text), 500000)]

# Ініціалізуємо лічильник підрядних речень
total_subordinate_count = 0

# Обробляємо кожну частину тексту окремо
for part in text_parts:
    subordinate_count = count_subordinate_clauses(part)
    total_subordinate_count += subordinate_count

print("Загальна кількість складнопідрядних речень:", total_subordinate_count)

#Загальна кількість складнопідрядних речень: 3750