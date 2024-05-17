import os

def split_corpus_into_files(corpus_path):
    # Read the corpus
    with open(corpus_path, 'r', encoding='utf-8') as f:
        corpus = f.read()

    # Split the corpus into texts based on empty lines
    texts = corpus.strip().split('\n\n')

    # Count the number of texts
    num_texts = len(texts)
    print("Total number of texts in corpus:", num_texts)

    # Create a directory to store the output files
    output_dir = os.path.join(os.path.dirname(corpus_path), 'corpus-uk-zh/separate_files_zh')
    os.makedirs(output_dir, exist_ok=True)

    # Write each group of 10 texts into separate files
    for i in range(0, num_texts, 10):
        filename = f"texts_{i//10}.txt"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(texts[i:i+10]))

        print(f"Saved texts {i+1} to {min(i+10, num_texts)} in {filename}")

# Example usage
corpus_path = 'corpus-uk-zh/TED2020.uk-zh.zh'  # Path to your corpus
split_corpus_into_files(corpus_path)
