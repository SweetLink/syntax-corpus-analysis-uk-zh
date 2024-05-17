import jieba.posseg as pseg

def count_verb_phrases(text):
    sentences = text.split('。')  # Розділити текст на речення

    total_verb_phrases = 0
    for sentence in sentences:
        words = pseg.cut(sentence.strip())  # Токенізація китайського речення
        verb_phrase_count = 0

        # Підрахунок кількості дієслівних фраз у кожному реченні
        for word, flag in words:
            if flag.startswith('v'):  # Якщо слово - дієслово
                verb_phrase_count += 1

        total_verb_phrases += verb_phrase_count

    return total_verb_phrases

# Завантажити корпус китайських текстів
with open('uk-zh.txt (1)/TED2020.uk-zh.zh', 'r', encoding='utf-8') as file:
    text = file.read()

verb_phrase_count = count_verb_phrases(text)
print("Кількість дієслівних фраз у корпусі: ", verb_phrase_count)

#Кількість дієслівних фраз у корпусі:  54091