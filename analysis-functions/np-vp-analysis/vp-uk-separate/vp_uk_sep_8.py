import spacy

# Завантажуємо модель для української мови
nlp = spacy.load("uk_core_news_sm")
nlp.max_length = 1500000 

def count_verb_phrases(text):
    doc = nlp(text)
    verb_phrases_count = 0

    for sent in doc.sents:
        for token in sent:
            if token.pos_ == "VERB" and token.dep_ == "root":
                verb_phrases_count += 1
            elif token.dep_ == "aux" and token.head.pos_ == "VERB":
                verb_phrases_count += 1

    return verb_phrases_count

# Завантажуємо корпус
corpus_path = "corpus-uk-zh/separate_files_uk/texts_7.txt"
with open(corpus_path, "r", encoding="utf-8") as file:
    corpus_text = file.read()

# Підрахунок кількості дієслівних фраз у корпусі
total_verb_phrases = count_verb_phrases(corpus_text)
print("Загальна кількість дієслівних фраз у корпусі:", total_verb_phrases)

#Загальна кількість дієслівних фраз у корпусі: 31