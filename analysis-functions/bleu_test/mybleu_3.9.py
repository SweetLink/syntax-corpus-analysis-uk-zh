# https://huggingface.co/spaces/evaluate-metric/bleu

import nltk
import evaluate
from nltk.translate.bleu_score import corpus_bleu
predictions = ["","", "", "", ""]
references = [
   [""],
    [""],
    [""],
    [""],
    [""]
]
bleu = evaluate.load("bleu")
results = bleu.compute(predictions=predictions, references=references)
print(results)

# {'bleu': 0.1756825820356824, 'precisions': [0.40540540540540543, 0.2318840579710145, 0.140625, 0.0847457627118644], 'brevity_penalty': 0.9602702338479381, 'length_ratio': 0.961038961038961, 'translation_length': 74, 'reference_length': 77}