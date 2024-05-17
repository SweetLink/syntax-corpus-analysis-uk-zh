# import spacy

# # Завантаження української моделі spaCy
# nlp = spacy.load("uk_core_news_sm")
# nlp.max_length = 2000000

# # Функція для підрахунку складних речень
# def count_complex_sentences(text):
#     doc = nlp(text)
#     compound_count = 0
#     complex_count = 0
    
#     for sentence in doc.sents:
#         if len(list(sentence)) >= 2:  # Якщо у реченні є дві або більше граматичних основ
#             if any(token.dep_ == 'conj' for token in sentence):  # Якщо є з'єднання
#                 compound_count += 1
#             elif any(token.dep_ == 'ccomp' or token.dep_ == 'xcomp' for token in sentence):  # Якщо є підречення
#                 complex_count += 1
    
#     return compound_count, complex_count

# Завантаження тексту з файлу
# with open("uk-zh.txt (1)/TED2020.uk-zh.uk", "r", encoding="utf-8") as file:
#     corpus_text = file.read()

# # Підрахунок складних речень у корпусі
# compound_sentences, complex_sentences = count_complex_sentences(corpus_text)

# print("Кількість складних речень (compound):", compound_sentences)
# print("Кількість складних речень (complex):", complex_sentences)

# Кількість складних речень (compound): 4935
# Кількість складних речень (complex): 2251


import spacy

# Завантаження українського модуля для spaCy
nlp = spacy.load("uk_core_news_sm")
nlp.max_length = 2000000

# Функція для визначення типу речення
def determine_sentence_type(sentence):
    # Визначення кількості головних і підрядних речень у реченні
    main_clauses = 0
    sub_clauses = 0
    for token in sentence:
        if token.dep_ == "ROOT":
            main_clauses += 1
        elif token.dep_ == "conj" and token.head.dep_ == "ROOT":
            main_clauses += 1
        elif token.dep_ == "ccomp" or token.dep_ == "advcl" and token.head.dep_ == "ROOT":
            sub_clauses += 1

    # Якщо є хоча б один головний та один підрядний зв'язок, це складне речення
    if main_clauses >= 1 and sub_clauses >= 1:
        return "complex"
    # Якщо є більше одного головного зв'язку, це складне речення
    elif main_clauses >= 2:
        return "compound"
    else:
        return "simple"

# Завантаження тексту з файлу
with open("uk-zh.txt (1)/TED2020.uk-zh.uk", "r", encoding="utf-8") as file:
    corpus = file.read()

# Обробка тексту і визначення кількості складних речень
doc = nlp(corpus)
complex_sentences_count = 0
for sentence in doc.sents:
    sentence_type = determine_sentence_type(sentence)
    if sentence_type == "compound" or sentence_type == "complex":
        complex_sentences_count += 1

# Виведення результату
print("Кількість складних речень у тексті:", complex_sentences_count)
# Кількість складних речень у тексті: 4987

# import spacy

# # Load Ukrainian language model
# nlp = spacy.load("uk_core_news_sm")
# nlp.max_length = 2000000

# def count_complex_sentences(corpus_file):
#     complex_sentence_count = 0

#     with open(corpus_file, "r", encoding="utf-8") as file:
#         corpus = file.read()

#     # Process text using spaCy
#     doc = nlp(corpus)

#     # Check each sentence for complexity
#     for sentence in doc.sents:
#         num_clauses = 0
#         for token in sentence:
#             if token.dep_ in ["conj", "ccomp", "advcl"]:
#                 num_clauses += 1
#         if num_clauses >= 1:
#             complex_sentence_count += 1

#     return complex_sentence_count

# corpus_file = "uk-zh.txt (1)/TED2020.uk-zh.uk"
# complex_sentence_count = count_complex_sentences(corpus_file)
# print("Total number of complex sentences:", complex_sentence_count)

#Total number of complex sentences: 7155


# import spacy

# # Load Ukrainian language model
# nlp = spacy.load("uk_core_news_sm")  # Use appropriate model for Ukrainian
# nlp.max_length = 2000000

# def count_composite_sentences(corpus_file):
#     composite_count = 0

#     with open(corpus_file, 'r', encoding='utf-8') as file:
#         corpus = file.read()

#     doc = nlp(corpus)

#     for sentence in doc.sents:
#         # Check if the sentence has more than one clause
#         if len([token for token in sentence if token.dep_ in ['ccomp', 'conj', 'advcl']]) > 1:
#             composite_count += 1

#     return composite_count

# corpus_file = "uk-zh.txt (1)/TED2020.uk-zh.uk"  # Path to your corpus file
# composite_sentences = count_composite_sentences(corpus_file)
# print("Total number of composite sentences:", composite_sentences)


#Total number of composite sentences: 3489