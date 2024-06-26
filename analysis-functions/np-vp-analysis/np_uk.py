import spacy

# Завантаження моделі мови українською
nlp = spacy.load("uk_core_news_sm")

def count_noun_phrases(text):
    doc = nlp(text)
    noun_phrase_count = 0
    for token in doc:
        if token.pos_ == 'NOUN' and token.dep_ == 'nsubj':
            noun_phrase_count += 1
    return noun_phrase_count

def main():
    # Зчитування корпусу тексту з файлу
    with open('uk-zh.txt (1)/TED2020.uk-zh.uk', 'r', encoding='utf-8') as file:
        corpus = file.read().splitlines()

    total_noun_phrases = 0
    for sentence in corpus:
        total_noun_phrases += count_noun_phrases(sentence)

    print("Загальна кількість іменникових фраз у корпусі:", total_noun_phrases)

if __name__ == "__main__":
    main()

#Загальна кількість іменникових фраз у корпусі: 6386