import re
from io import open

with open('es_ancora-ud-train.conllu', 'r', encoding='ISO-8859-1') as file:
    train = file.read()
with open('es_ancora-ud-dev.conllu', 'r', encoding='ISO-8859-1') as file:
    dev = file.read()
with open('es_ancora-ud-test.conllu', 'r', encoding='ISO-8859-1') as file:
    test = file.read()

# sample verb = '10	hace	hacer	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	9	advcl	_	_'
verb_re = r'([\d]+\t[A-Za-z]+\t[A-Za-z]+\tVERB\t_\t[A-Za-z=|0-9]*\t[\d]+\t[a-z]+\t_\t_)'
verbs_found = re.findall(verb_re, train) + re.findall(verb_re, dev) + re.findall(verb_re, test)
with open('verbs.txt', mode='wt', encoding='utf-8') as file:
    file.write('\n'.join(verbs_found))
