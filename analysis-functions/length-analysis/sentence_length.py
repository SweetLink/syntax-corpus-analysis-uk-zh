import spacy
from spacy.lang.uk import Ukrainian
from spacy.lang.zh import Chinese

# Завантажити моделі spacy для української та китайської мов
nlp_zh = spacy.load("zh_core_web_md")
nlp_uk = spacy.load("uk_core_news_md")

# Збільшити максимальну довжину речення для обох моделей
nlp_uk.max_length = 1500000
nlp_zh.max_length = 1500000

# Функція для обчислення довжини речень
def count_sentence_lengths(text, nlp):
  """
  Функція, яка приймає текст та модель spacy як аргументи і повертає список довжин речень та їхню середню.

  Args:
      text (str): Текст, який потрібно обробити.
      nlp (spacy.Language): Модель spacy для мови тексту.

  Returns:
      tuple: Кортеж, що містить список довжин речень та їхню середню.
  """
  doc = nlp(text)
  sentence_lengths = []
  for sentence in doc.sents:
    sentence_lengths.append(len(sentence))
  return sentence_lengths, sum(sentence_lengths) / len(sentence_lengths)

# Обробка китайського корпусу текстів
with open('uk-zh.txt (1)/TED2020.uk-zh.zh', 'r', encoding='utf-8') as f:
  chinese_text = f.read()

chinese_sentence_lengths, chinese_avg_sentence_length = count_sentence_lengths(chinese_text, nlp_zh)
print("Довжини речень у китайському корпусі:", chinese_sentence_lengths)
print("Середня довжина речення в китайському корпусі:", chinese_avg_sentence_length)

# Обробка українського корпусу текстів
with open('uk-zh.txt (1)/TED2020.uk-zh.uk', 'r', encoding='utf-8') as f:
  ukrainian_text = f.read()

ukrainian_sentence_lengths, ukrainian_avg_sentence_length = count_sentence_lengths(ukrainian_text, nlp_uk)
print("Довжини речень у українському корпусі:", ukrainian_sentence_lengths)
print("Середня довжина речення в українському корпусі:", ukrainian_avg_sentence_length)
