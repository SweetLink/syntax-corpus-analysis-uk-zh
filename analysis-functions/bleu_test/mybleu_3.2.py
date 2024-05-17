# https://huggingface.co/spaces/evaluate-metric/bleu

import nltk
import evaluate
from nltk.translate.bleu_score import corpus_bleu
predictions = ["Але цей візок - як чарівна іграшка.","Він дозволяє мені гуляти з вітром.", "І це так приємно мати можливість вийти на вулицю!", "Я така щаслива, що знову вільна, але люди на вулиці ставляться до мене по-іншому.", "Вони ставляться до мене так, ніби я невидима, ніби я ношу плащ-невидимку.", "Вони дивляться на мене з упередженням, ніби я в інвалідному візку і я трохи безладний."]
references = [
   ["Але ця коляска як чарівна іграшка,"], 
   ["бо з нею я можу вибиратися на свіже повітря."],
    ["Крім того, можливість вийти на вулицю це дуже класно!"],
    ["Хоча я й щаслива знову бути вільною, але ставлення до мене з боку інших тепер зовсім інше."],
    ["Здається, ніби я для них прозора, що, ніби одягнена у плащ-невидимку."],
    ["Вони дивляться косо на мене з упередженням, думаючи, що, якщо сиджу в інвалідному візку, то обов’язково обмежена у всьому."]
]
bleu = evaluate.load("bleu")
results = bleu.compute(predictions=predictions, references=references)
print(results)

# {'bleu': 0.1478819430721911, 'precisions': [0.5, 0.2647058823529412, 0.12903225806451613, 0.05357142857142857], 'brevity_penalty': 0.8503033063369504, 'length_ratio': 0.8604651162790697, 'translation_length': 74, 'reference_length': 86}