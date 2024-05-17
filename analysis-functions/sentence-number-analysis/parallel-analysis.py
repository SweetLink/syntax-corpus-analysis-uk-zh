import spacy
import re
import requests

nlp_zh = spacy.load("zh_core_web_md")
nlp_uk = spacy.load("uk_core_news_md")


def count_sentences(corpus_url):
  """Counts the number of sentences in a Chinese-Ukrainian corpus from a URL.

  Args:
    corpus_url: The URL of the online corpus.

  Returns:
    A dictionary with keys 'chinese_sentences' and 'ukrainian_sentences' containing respective counts.
  """
  chinese_sentences = 0
  ukrainian_sentences = 0

  # Fetch the corpus content from the URL
  try:
    response = requests.get(corpus_url)
    response.raise_for_status()  # Raise exception for non-2xx status codes
    #corpus_text = response.content.decode('utf-8')
  except requests.exceptions.RequestException as e:
    print(f"Error fetching corpus: {e}")
    return {'chinese_sentences': 0, 'ukrainian_sentences': 0}

  # Separate counts for Chinese and Ukrainian sentence endings
  chinese_sentences += len(re.findall(r'[。！？；，]', corpus_url))
  ukrainian_sentences += len(re.findall(r'\n', corpus_url))
  return {'chinese_sentences': chinese_sentences, 'ukrainian_sentences': ukrainian_sentences}


# Example usage
corpus_url = 'https://object.pouta.csc.fi/OPUS-TED2020/v1/parsed/uk.zip'  # Replace with your actual URL
sentence_counts = count_sentences(corpus_url)
print("Number of Chinese sentences:", sentence_counts['chinese_sentences'])
print("Number of Ukrainian sentences:", sentence_counts['ukrainian_sentences'])
