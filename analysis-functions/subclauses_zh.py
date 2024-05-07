import jieba

def count_subordinate_clauses(text):
    # Визначення розділових знаків для китайської мови
    punctuation = "。！？"
    
    # Розбиваємо текст на речення
    sentences = []
    temp = ''
    for char in text:
        temp += char
        if char in punctuation:
            sentences.append(temp.strip())
            temp = ''
    if temp:
        sentences.append(temp.strip())
    
    # Підрахунок підрядних частин у кожному реченні
    subordinate_count = 0
    for sentence in sentences:
        words = jieba.lcut(sentence)  # Розбиваємо речення на слова з використанням jieba
        for word in words:
            if word == "，" or word == "的" or word == "是" or word == "了":
                subordinate_count += 1
                break

    return subordinate_count

# Зчитуємо корпус з файлу
with open('uk-zh.txt (1)/TED2020.uk-zh.zh', 'r', encoding='utf-8') as file:
    corpus = file.read()

# Рахуємо підрядні частини у корпусі
total_subordinate_clauses = count_subordinate_clauses(corpus)
print("Загальна кількість підрядних частин у корпусі:", total_subordinate_clauses)

#Загальна кількість підрядних частин у корпусі: 1892

 
