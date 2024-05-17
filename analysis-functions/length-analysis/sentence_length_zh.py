import re

def average_sentence_length(text):
    # Розділити текст на речення
    sentences = re.split(r'[。！？]', text)
    
    total_words = 0
    total_sentences = 0
    
    # Підрахунок кількості слів у кожному реченні
    for sentence in sentences:
        # Видалити можливі пробіли з початку та кінця речення
        sentence = sentence.strip()
        # Пропустити порожні речення
        if sentence:
            # Розділити речення на слова
            words = sentence.split()
            # Додати кількість слів у реченні до загального числа слів
            total_words += len(words)
            # Збільшити лічильник речень
            total_sentences += 1
    
    # Обчислити середню довжину речення
    if total_sentences > 0:
        average_length = total_words / total_sentences
    else:
        average_length = 0
    
    return average_length

# Зчитати китайський текст з файлу
with open("uk-zh.txt (1)/TED2020.uk-zh.zh", "r", encoding="utf-8") as file:
    chinese_text = file.read()

# Визначити середню довжину речення
avg_length = average_sentence_length(chinese_text)

print("Середня довжина речення (в словах):", avg_length)

#Середня довжина речення (в словах): 11.334656084656086