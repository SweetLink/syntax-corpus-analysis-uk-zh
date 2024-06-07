# https://huggingface.co/spaces/evaluate-metric/bleu

import nltk
import evaluate
from nltk.translate.bleu_score import corpus_bleu
predictions = ["Ми навчилися серйозно ставитися до кожного слова нашого життя -- Девіс 2009, TEDx Women Я почала робити деякі роботи які мали на меті передати внутрішню радість і свободу перебування в інвалідному візку і я називаю його енергетичним кріслом тому що я можу взяти світ за роги","Я намагаюся передати те що я відчуваю всередині змінити те як я думав про себе коли вперше почав їздити на візку через позаконтекстну фотографію", "Візок став чимось на чому я можу писати і малювати", "Коли я почала залишати на собі слід щастя і свободи я була настільки схвильована що зовнішній світ відгукнувся на мої роботи", "Ці роботи здається відкривають нові горизонти і ведуть до трансформації мистецтва"]
references = [
   ["Ми навчилися серйозно ставитися до кожного слова яке пишемо про своє життя ——Davis 2009, опубліковано в TEDx Women Я почала проводити різні заходи аби передати всім почуття внутрішньої радості і свободи які маєш перебуваючи в інвалідному візку Я називаю його кріслом сили тому що можу пересуватися в ньому по всьому по світу"],
    ["Я намагалася якнайкраще передати свої внутрішні відчуття через нестандартне зображення щоб змінити стереотип про себе коли я опинився в інвалідному візку"],
    ["Він дав мені змогу писати та малювати"],
    ["Коли я почала буквально залишати сліди свого внутрішнього щастя і свободи то і зовнішній світ відгукнувся на мої роботи І я була цьому безмежно рада"],
    ["Ці твори ніби відкрили мені нові горизонти й направили в бік мистецтва"]
]
bleu = evaluate.load("bleu")
results = bleu.compute(predictions=predictions, references=references)
print(results)

# {'bleu': 0.18742404838544888, 'precisions': [0.49557522123893805, 0.25, 0.14563106796116504, 0.08163265306122448], 'brevity_penalty': 0.9567168655138897, 'length_ratio': 0.9576271186440678, 'translation_length': 113, 'reference_length': 118}