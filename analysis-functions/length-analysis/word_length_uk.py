def average_sentence_length(corpus_file):
    total_chars = 0
    total_sentences = 0

    with open(corpus_file, 'r', encoding='utf-8') as file:
        for line in file:
            # Враховуємо тільки непорожні рядки (речення)
            if line.strip():
                total_chars += len(line.strip())
                total_sentences += 1

    if total_sentences == 0:
        return 0  # Перевірка на пустий файл

    return total_chars / total_sentences

corpus_file = "uk-zh.txt (1)/TED2020.uk-zh.uk"
average_length = average_sentence_length(corpus_file)
print("Середня довжина речення в корпусі: {:.2f} літер".format(average_length))

#Середня довжина речення в корпусі: 84.32 літер