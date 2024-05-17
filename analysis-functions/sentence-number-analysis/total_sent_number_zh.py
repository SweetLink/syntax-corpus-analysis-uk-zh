# import jieba
# import re

# def count_sentences(text):
#     # Розділити текст на речення за допомогою регулярного виразу
#     sentences = re.split(r'[。！？]', text)
#     # Видалити порожні речення
#     sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
#     return len(sentences)

# def read_file(filepath):
#     with open(filepath, 'r', encoding='utf-8') as file:
#         return file.read()

# def main():
#     corpus_path = "uk-zh.txt (1)/TED2020.uk-zh.zh"
#     chinese_text = read_file(corpus_path)
#     # Токенізувати текст за допомогою jieba
#     chinese_sentences = list(jieba.cut(chinese_text))
#     chinese_text = " ".join(chinese_sentences)
#     # Підрахунок кількості речень
#     num_sentences = count_sentences(chinese_text)
#     print("Загальна кількість речень в корпусі:", num_sentences)

# if __name__ == "__main__":
#     main()

#Загальна кількість речень в корпусі: 3024 


# import jieba

# def count_sentences(text):
#     # Розділяємо текст на токени
#     tokens = jieba.cut(text, cut_all=False)
    
#     # Підрахунок кількості речень
#     sentence_count = 0
#     for token in tokens:
#         # Перевіряємо, чи токен закінчується на кінцевий розділовий знак речення
#         if token.endswith(('。', '？', '！', '；')):
#             sentence_count += 1
    
#     return sentence_count

# # Функція для зчитування тексту з файлу
# def read_file(filename):
#     with open(filename, 'r', encoding='utf-8') as file:
#         return file.read()

# # Шлях до файлу з китайським текстом
# file_path = "uk-zh.txt (1)/TED2020.uk-zh.zh"

# # Зчитуємо текст з файлу
# chinese_text = read_file(file_path)

# # Отримуємо кількість речень у тексті
# sentence_count = count_sentences(chinese_text)
# print("Кількість речень в корпусі китайською мовою:", sentence_count)

#Кількість речень в корпусі китайською мовою: 3048

# import spacy

# def count_sentences(file_path):
#     nlp = spacy.blank("zh")
#     sentencizer = nlp.add_pipe("sentencizer")
#     with open(file_path, "r", encoding="utf-8") as file:
#         text = file.read()
#         doc = nlp(text)
#         # Рахуємо кількість речень
#         sentence_count = len(list(doc.sents))
#     return sentence_count

# file_path = "uk-zh.txt (1)/TED2020.uk-zh.zh"
# total_sentences = count_sentences(file_path)
# print("Total number of sentences in the corpus:", total_sentences)

#Total number of sentences in the corpus: 3165

# def count_sentences(corpus_file):
#   """
#   Counts the number of sentences in a Chinese corpus with proper boundaries.

#   Args:
#       corpus_file: Relative path to the corpus file (e.g., "uk-zh.txt (1)/TED2020.uk-zh.zh").

#   Returns:
#       The total number of sentences in the corpus.
#   """
#   total_sentences = 0
#   with open(corpus_file, 'r', encoding='utf-8') as f:
#     # Use jieba for Chinese word segmentation
#     import jieba

#     # Define sentence ending punctuations (modify if needed)
#     sentence_endings = "！？｡。'' "

#     # Additional structural cues for sentence boundaries
#     structural_cues = ["但是", "然而", "因此", "所以", "不过"]  # Modify and expand as needed

#     for line in f:
#       # Segment the line into words
#       words = jieba.cut(line.strip())
#       # Track if the previous word ended a sentence
#       prev_ends_sentence = False
#       for word in words:
#         # Check for punctuation and structural cues
#         if (word in sentence_endings) or (word in structural_cues and not prev_ends_sentence):
#           total_sentences += 1
#           prev_ends_sentence = True
#         else:
#           prev_ends_sentence = False
#   return total_sentences

# # Example usage
# corpus_file = "uk-zh.txt (1)/TED2020.uk-zh.zh"
# number_of_sentences = count_sentences(corpus_file)
# print("Total number of sentences:", number_of_sentences)

#Total number of sentences: 3758
import jieba

def is_sentence_ending(char):
  # Define a set of common Chinese sentence ending punctuations
  endings = "！？｡。;；：﹑﹑"
  return char in endings

def count_sentences(corpus_file):
  """Counts the total number of sentences in a Chinese corpus.

  Args:
    corpus_file: The relative path to the corpus file.

  Returns:
    The total number of sentences in the corpus.
  """

  sentence_count = 0
  with open(corpus_file, 'r', encoding='utf-8') as f:
    for line in f:
      # Segment the line into words
      words = jieba.cut(line.strip())
      # Iterate through each character
      for char in words:
        if is_sentence_ending(char):
          sentence_count += 1

  return sentence_count

# Example usage
corpus_file = "uk-zh.txt (1)/TED2020.uk-zh.zh"
total_sentences = count_sentences(corpus_file)
print(f"Total number of sentences: {total_sentences}")

#Total number of sentences: 3514