import re

def count_sov_sentences(file_path):
    sov_count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', line.strip())
            for sentence in sentences:
                words = sentence.split()
                if len(words) >= 3 and words[0].endswith('ся') and words[1].endswith('ся'):
                    sov_count += 1
    return sov_count

file_path = 'uk-zh.txt (1)/TED2020.uk-zh.uk'
sov_sentences_count = count_sov_sentences(file_path)
print("Кількість речень зі схемою SOV в корпусі: ", sov_sentences_count)

#Кількість речень зі схемою SOV в корпусі:  1