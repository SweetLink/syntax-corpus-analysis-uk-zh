import re

def sentence_length(text):
    sentences = re.split(r'[.!?]', text)
    total_words = sum(len(sentence.split()) for sentence in sentences)
    average_length = total_words / len(sentences)
    return average_length

def main():
    # Зчитуємо текст з файлу
    with open("uk-zh.txt (1)/TED2020.uk-zh.uk", "r", encoding="utf-8") as file:
        text = file.read()

    avg_length = sentence_length(text)
    print("Середня довжина речення за кількістю слів:", avg_length)

if __name__ == "__main__":
    main()


#uk-zh.txt (1)/TED2020.uk-zh.uk
#Середня довжина речення за кількістю слів: 11.82978575885738
