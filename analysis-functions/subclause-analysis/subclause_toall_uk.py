import spacy

def count_subordinate_clauses(text):
    # Завантаження української моделі spaCy
    nlp = spacy.load("uk_core_news_sm")
    nlp.max_length = 2000000

    # Обробка тексту за допомогою spaCy
    doc = nlp(text)

    # Кількість речень у корпусі
    total_sentences = len(list(doc.sents))
    # Кількість підрядних речень
    total_subordinate_clauses = 0

    # Паттерн для знаходження підрядних речень
    sub_patterns = ["що", "як", "коли", "де", "чому", "хто", "щоб"]

    for sentence in doc.sents:
        # Пошук підрядних речень
        for token in sentence:
            if token.text.lower() in sub_patterns and token.dep_ == "mark":
                total_subordinate_clauses += 1
                break

    return total_subordinate_clauses, total_sentences

# Зчитування тексту з файлу
with open('uk-zh.txt (1)/TED2020.uk-zh.uk', 'r', encoding='utf-8') as file:
    text = file.read()

# Виклик функції для підрахунку підрядних речень
subordinate_clauses, total_sentences = count_subordinate_clauses(text)

# Визначення відношення кількості підрядних речень до загальної кількості речень
if total_sentences > 0:
    ratio = subordinate_clauses / total_sentences
    print("Частотність утворення складнопідрядних речень: {:.2f}%".format(ratio * 100))
else:
    print("Немає речень у тексті.")


#Частотність утворення складнопідрядних речень: 25.33%