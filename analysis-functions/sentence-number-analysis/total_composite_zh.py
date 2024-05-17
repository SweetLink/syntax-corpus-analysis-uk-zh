import jieba
import re

def count_composite_sentences(text):
    # Tokenize text into sentences
   
    sentences = re.split(r'[！？｡。;；：﹑﹑]', text)

    # Initialize count for composite sentences
    composite_count = 0

    # Loop through each sentence
    for sentence in sentences:
        # Tokenize sentence into clauses
        clauses = re.split(r'[，;；:]', sentence)
        
        # Count the number of clauses
        num_clauses = len(clauses)

        # If the number of clauses is more than 1, it's a composite sentence
        if num_clauses > 1:
            composite_count += 1

    return composite_count

# Read the Chinese corpus file
corpus_file = "uk-zh.txt (1)/TED2020.uk-zh.zh"

with open(corpus_file, "r", encoding="utf-8") as file:
    corpus_text = file.read()

# Tokenize sentences using jieba
corpus_sentences = list(jieba.cut(corpus_text))

# Join the tokenized sentences into a single string
corpus_text = ''.join(corpus_sentences)

# Count composite sentences
composite_sentence_count = count_composite_sentences(corpus_text)

print("Total number of composite sentences:", composite_sentence_count)

#Total number of composite sentences: 1957


#Total number of composite sentences: 1777





# import jieba

# def is_punctuation(char):
#     # Check if the character is a Chinese punctuation mark
#     punctuation_marks = "。？！；"
#     return char in punctuation_marks

# def find_subject_object(sentence_tokens):
#     subject = None
#     object_ = None
#     for token in sentence_tokens:
#         if 'n' in token[1] or 'r' in token[1]:  # Noun or pronoun
#             if subject is None:
#                 subject = token[0]
#             else:
#                 object_ = token[0]
#                 break
#     return subject, object_

# def count_composite_sentences(corpus_file):
#     composite_sentence_count = 0
#     with open(corpus_file, 'r', encoding='utf-8') as file:
#         for line in file:
#             sentences = jieba.cut(line.strip())
#             sentence_tokens = [(token, 'unk') for token in sentences]  # Assume all tokens as unknown
#             subject, object_ = None, None
#             for token in sentence_tokens:
#                 if is_punctuation(token[0]):
#                     if subject and object_:
#                         composite_sentence_count += 1
#                     subject, object_ = None, None
#                 elif not subject:
#                     subject, object_ = find_subject_object(sentence_tokens)
#     return composite_sentence_count

# corpus_file = "uk-zh.txt (1)/TED2020.uk-zh.zh"
# composite_sentence_count = count_composite_sentences(corpus_file)
# print("Total number of composite sentences:", composite_sentence_count)
#Total number of composite sentences: 3048