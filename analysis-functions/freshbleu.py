import nltk
import evaluate
from nltk.translate.bleu_score import corpus_bleu
predictions = ["hello there general kenobi","foo bar foobar"]
references = [
   ["hello there general kenobi"],
    ["foo bar foobar"]
]
bleu = evaluate.load("bleu")
results = bleu.compute(predictions=predictions, references=references)
print(results)