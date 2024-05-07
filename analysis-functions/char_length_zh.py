
import re

def count_chars(text):
    # Видаляємо всі символи, окрім китайських ієрогліфів
    chinese_chars = re.findall(r'[\u4e00-\u9fff]', text)
    return len(chinese_chars)

def average_sentence_length(corpus_file):
    with open(corpus_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    total_chars = 0
    total_sentences = 0

    for line in lines:
        # Розділяємо речення за китайськими розділовими знаками
        sentences = re.split('[。！？]', line.strip())
        total_sentences += len(sentences)
        
        for sentence in sentences:
            # Ігноруємо порожні речення
            if sentence.strip():
                total_chars += count_chars(sentence)

    if total_sentences == 0:
        return 0
    else:
        return total_chars / total_sentences

corpus_file = "uk-zh.txt (1)/TED2020.uk-zh.zh"
avg_length = average_sentence_length(corpus_file)
print("Середня довжина речення: {:.2f} ієрогліфів".format(avg_length))

#Середня довжина речення: 18.58 ієрогліфів