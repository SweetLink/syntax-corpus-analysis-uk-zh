import jieba.posseg as pseg

def count_noun_phrases(text):
    words = pseg.cut(text)  # Розбиваємо текст на токени та частини мови
    noun_phrases = []
    current_phrase = ''
    for word, pos in words:
        if pos.startswith('n'):  # Перевіряємо, чи є це іменник
            current_phrase += word
        elif current_phrase:
            noun_phrases.append(current_phrase)
            current_phrase = ''
    if current_phrase:  # Додаємо останню фразу, якщо вона була у тексті
        noun_phrases.append(current_phrase)
    return len(noun_phrases)

def main():
    # Зчитування тексту з файлу
    with open("corpus-uk-zh/corpus-uk-zh/separate_files_zh/texts_5.txt", "r", encoding="utf-8") as file:
        text = file.read()

    # Розділення тексту на речення
    sentences = text.split('。')  # Припускаємо, що кінець речення - крапка

    total_noun_phrases = 0
    for sentence in sentences:
        total_noun_phrases += count_noun_phrases(sentence)

    print("Загальна кількість іменникових фраз у сегменті корпусу:", total_noun_phrases)

if __name__ == "__main__":
    main()

#Загальна кількість іменникових фраз у сегменті корпусу: 2519