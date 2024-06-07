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