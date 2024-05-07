import jieba
import re

def count_subordinate_clauses(text):
    # Токенізуємо китайський текст
    sentences = re.split(r'[。！？]', text)  # розбиваємо текст на речення за допомогою знаків кінця речення
    
    total_sentences = len(sentences)
    subordinate_count = 0
    
    # Проходимося по кожному реченню
    for sentence in sentences:
        # Розділяємо речення на токени
        tokens = jieba.cut(sentence)
        tokens = [token for token in tokens]
        
        # Перевіряємо, чи є у реченні підрядне речення
        if '的' in tokens:  # можна додати інші ключові слова для підрядних речень
            subordinate_count += 1
    
    # Повертаємо відношення кількості підрядних речень до загальної кількості речень
    return subordinate_count / total_sentences

# Завантажуємо корпус китайського тексту
with open('uk-zh.txt (1)/TED2020.uk-zh.zh', 'r', encoding='utf-8') as file:
    chinese_corpus = file.read()

subordinate_frequency = count_subordinate_clauses(chinese_corpus)
print("Частотність утворення складнопідрядних речень: {:.2f}%".format(subordinate_frequency))


#Частотність утворення складнопідрядних речень: 0.0922619047619047
#Частотність утворення складнопідрядних речень: 0.09%