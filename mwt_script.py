import re
import numpy as np
import csv
import random

mwt_strings = []

starter = """# sent_id = 0
# text = juntarse.
1-2	juntarse	_	_	_	_	_	_	_	SpaceAfter=No
1	juntar	juntar	VERB	_	VerbForm=Inf	0	root	_	_
2	se	él	PRON	_	Case=Acc|Person=3|PrepCase=Npr|PronType=Prs|Reflex=Yes	1	obj	_	_
3	.	.	PUNCT	_	PunctType=Peri	1	punct	_	_

# sent_id = 0
# text = Juntarse.
1-2	Juntarse	_	_	_	_	_	_	_	SpaceAfter=No
1	Juntar	juntar	VERB	_	VerbForm=Inf	0	root	_	_
2	se	él	PRON	_	Case=Acc|Person=3|PrepCase=Npr|PronType=Prs|Reflex=Yes	1	obj	_	_
3	.	.	PUNCT	_	PunctType=Peri	1	punct	_	_"""

mwt_strings.append(starter)

with open('verbs.txt', 'r') as file:
    verbs_string = file.read()

# sample verb = '10	hace	hacer	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	9	advcl	_	_'
# verb_re = r'[\d]+(\t[A-Za-z]+\t[A-Za-z]+\tVERB\t_\t[A-Za-z=|0-9]*\t[\d]+\t[a-z]+\t_\t_)'
verbs_found = verbs_string.splitlines()
print('The number of verbs found was:', len(verbs_found))
for i, j, in enumerate(verbs_found):
    j_new = re.sub(r'\t[\d]+', '\t0', j)
    verbs_found[i] = "1" + j_new

unique_verbs = list(np.unique(verbs_found))
inf_ger_verbs = [verb for verb in unique_verbs if re.search(r'VerbForm=(?:(?:Ger)|(?:Inf))', verb) is not None]

dir_obj_add = ["2\tme\tyo\tPRON\t_\tCase=Dat|Number=Sing|Person=1|PrepCase=Npr|PronType=Prs|Reflex=Yes\t1\tiobj\t_\t_",
               "2\tme\tyo\tPRON\t_\tCase=Dat|Number=Sing|Person=1|PrepCase=Npr|PronType=Prs\t1\tobj\t_\t_",
               "2\tte\ttú\tPRON\t_\tCase=Dat|Number=Sing|Person=2|PrepCase=Npr|PronType=Prs|Reflex=Yes\t1\tiobj\t_\t_",
               "2\tte\ttú\tPRON\t_\tCase=Dat|Number=Sing|Person=2|PrepCase=Npr|PronType=Prs\t1\tobj\t_\t_",
               "2\tle\tél\tPRON\t_\tCase=Dat|Number=Sing|Person=3|PronType=Prs\t1\tobj\t_\t_",
               "2\tse\tél\tPRON\t_\tCase=Acc|Person=3|PrepCase=Npr|PronType=Prs|Reflex=Yes\t1\tobj\t_\t_",
               "2\tse\tél\tPRON\t_\tCase=Acc|Person=3|PrepCase=Npr|PronType=Prs\t1\tobj\t_\t_",
               "2\tse\tél\tPRON\t_\tCase=Acc|Person=3|PrepCase=Npr|PronType=Prs|Reflex=Yes\t1\texpl:pv\t_\t_",
               "2\tse\tél\tPRON\t_\tCase=Acc|Person=3|PrepCase=Npr|PronType=Prs\t1\texpl:pv\t_\t_",
               "2\tnos\tyo\tPRON\t_\tCase=Dat|Number=Plur|Person=1|PrepCase=Npr|PronType=Prs|Reflex=Yes\t1\tiobj\t_\t_",
               "2\tnos\tyo\tPRON\t_\tCase=Dat|Number=Plur|Person=1|PrepCase=Npr|PronType=Prs\t1\tobj\t_\t_",
               "2\tles\tél\tPRON\t_\tCase=Dat|Number=Plur|Person=3|PronType=Prs\t1\tobj\t_\t_",
               "2\tla\tél\tPRON\t_\tCase=Acc|Gender=Fem|Number=Sing|Person=3|PrepCase=Npr|PronType=Prs\t1\tobj\t_\t_",
               "2\tlo\tél\tPRON\t_\tCase=Acc|Gender=Masc|Number=Sing|Person=3|PrepCase=Npr|PronType=Prs\t1\tobj\t_\t_",
               "2\tlas\tél\tPRON\t_\tCase=Acc|Gender=Fem|Number=Plur|Person=3|PrepCase=Npr|PronType=Prs\t1\tobj\t_\t_",
               "2\tlos\tél\tPRON\t_\tCase=Acc|Gender=Masc|Number=Plur|Person=3|PrepCase=Npr|PronType=Prs\t1\tobj\t_\t_"]

ind_obj_pron = ["2\tme\tyo\tPRON\t_\tCase=Dat|Number=Sing|Person=1|PrepCase=Npr|PronType=Prs|Reflex=Yes\t1"
                "\tiobj\t_\t_ ",
                "2\tte\ttú\tPRON\t_\tCase=Dat|Number=Sing|Person=2|PrepCase=Npr|PronType=Prs\t1\tiobj\t_\t_",
                "2\tle\tél\tPRON\t_\tCase=Dat|Number=Sing|Person=3|PronType=Prs\t1\tiobj\t_\t_",
                "2\tse\tél\tPRON\t_\tCase=Acc|Person=3|PrepCase=Npr|PronType=Prs|Reflex=Yes\t1\tiobj\t_\t_",
                "2\tnos\tyo\tPRON\t_\tCase=Dat|Number=Plur|Person=1|PrepCase=Npr|PronType=Prs\t1\tiobj\t_\t_",
                "2\tles\tél\tPRON\t_\tCase=Dat|Number=Sing|Person=3|PronType=Prs\t1\tiobj\t_\t_"]

ind_obj_prep = ["3\tla\tél\tPRON\t_\tCase=Acc|Gender=Fem|Number=Sing|Person=3|PrepCase=Npr|PronType=Prs\t1\tiobj\t_\t_",
                "3\tlo\tél\tPRON\t_\tCase=Acc|Gender=Masc|Number=Sing|Person=3|PrepCase=Npr|PronType=Prs\t1\tiobj\t_\t_",
                "3\tlas\tél\tPRON\t_\tCase=Acc|Gender=Fem|Number=Plur|Person=3|PrepCase=Npr|PronType=Prs\t1\tiobj\t_\t_",
                "3\tlos\tél\tPRON\t_\tCase=Acc|Gender=Masc|Number=Plur|Person=3|PrepCase=Npr|PronType=Prs\t1\tiobj\t_\t_"]

sent_id = "# sent_id = 0"
text = "# text = "
period_dir = "3	.	.	PUNCT	_	PunctType=Peri	1	punct	_	_"
period_indir = "4	.	.	PUNCT	_	PunctType=Peri	1	punct	_	_"
verbs_list = []

accent_letter = {'a': 'á',
                 'e': 'é',
                 'i': 'í',
                 'o': 'ó',
                 'u': 'ú'}

for verb in inf_ger_verbs:
    for i in range(4):
        verb_matches = re.findall(r'[\d]+\t([A-Za-z]+)\t', verb)
        verb_text = verb_matches[0].lower()
        if verbs_list.count(verb_text) >= 4:
            break
        verbs_list.append(verb_text)

        if random.randint(0, 3) < 1:
            continue

        cap = random.randint(0, 1)
        if cap == 1:
            capital_text = verb_text.capitalize()
            capital_verb = verb.replace(verb_text, capital_text)
            verb_text, verb = capital_text, capital_verb

        dir_ind = random.randint(0, 1)
        if dir_ind == 0:
            add = random.choice(dir_obj_add)
            if re.search('VerbForm=Inf', verb) is None:
                verb_text = verb_text[:len(verb_text) - 4] + accent_letter[verb_text[len(verb_text) - 4]] + verb_text[len(verb_text) - 3:]
            add_text = re.findall(r'[\d]+\t([A-Za-z]+)\t', add)[0]
            submitted_text = text + verb_text + add_text + "."
            mwt_text = "1-2\t" + verb_text + add_text + "\t_\t_\t_\t_\t_\t_\t_\tSpaceAfter=No"
            text_parts = [sent_id, submitted_text, mwt_text, verb, add, period_dir]
        else:
            if re.search('VerbForm=Inf', verb) is None:
                verb_text = verb_text[:len(verb_text) - 4] + accent_letter[verb_text[len(verb_text) - 4].lower()] + \
                            verb_text[len(verb_text) - 3:]
            elif re.search('VerbForm=Inf', verb) is not None:
                if verb_text[-1] != 'r':
                    break
                verb_text = verb_text[:len(verb_text) - 2] + accent_letter[verb_text[len(verb_text) - 2].lower()] + \
                            verb_text[len(verb_text) - 1]
            add_pron = random.choice(ind_obj_pron)
            add_pron_text = re.findall(r'[\d]+\t([A-Za-z]+)\t', add_pron)[0]
            add_prep = random.choice(ind_obj_prep)
            add_prep_text = re.findall(r'[\d]+\t([A-Za-z]+)\t', add_prep)[0]
            submitted_text = text + verb_text + add_pron_text + add_prep_text
            mwt_text = "1-3\t" + verb_text + add_pron_text + add_prep_text + "\t_\t_\t_\t_\t_\t_\t_\tSpaceAfter=No"
            text_parts = [sent_id, submitted_text, mwt_text, verb, add_pron, add_prep, period_indir]

        new_entry = '\n'.join(text_parts)
        if new_entry not in mwt_strings:
            mwt_strings.append(new_entry)

reflex_te = ["2\tte\ttú\tPRON\t_\tCase=Dat|Number=Sing|Person=2|PrepCase=Npr|PronType=Prs|Reflex=Yes\t1\texpl:pv\t_\t_",
             "2\tte\ttú\tPRON\t_\tCase=Dat|Number=Sing|Person=2|PrepCase=Npr|PronType=Prs|Reflex=Yes\t1\tiobj\t_\t_"]

reflex_se = ["2\tse\tél\tPRON\t_\tCase=Acc|Person=3|PrepCase=Npr|PronType=Prs|Reflex=Yes\t1\tobj\t_\t_",
             "2\tse\tél\tPRON\t_\tCase=Acc|Person=3|PrepCase=Npr|PronType=Prs|Reflex=Yes\t1\texpl:pv\t_\t_",
             "2\tse\tél\tPRON\t_\tCase=Acc|Person=3|PrepCase=Npr|PronType=Prs|Reflex=Yes\t1\tiobj\t_\t_"]

con_obj_add = ["2\tme\tyo\tPRON\t_\tCase=Dat|Number=Sing|Person=1|PrepCase=Npr|PronType=Prs\t1\tiobj\t_\t_",
               "2\tte\ttú\tPRON\t_\tCase=Dat|Number=Sing|Person=2|PrepCase=Npr|PronType=Prs\t1\tiobj\t_\t_",
               "2\tse\tél\tPRON\t_\tCase=Acc|Person=3|PrepCase=Npr|PronType=Prs\t1\tiobj\t_\t_",
               "2\tnos\tyo\tPRON\t_\tCase=Dat|Number=Plur|Person=1|PrepCase=Npr|PronType=Prs\t1\tiobj\t_\t_"]

with open("imperatives.csv", 'r') as imperative_list:
    imperative_titles = ['infinitive', 'tu', 'usted', 'ustedes']
    imperative_conjugates = imperative_list.readlines()

for row in imperative_conjugates:
    row_forms = row.split(',')
    ustedes = row_forms[3]
    row_forms[3] = ustedes[:-1]
    for j in range(3):
        form = random.choice(['tu', 'usted', 'ustedes'])
        cap = random.randint(0, 1)
        clause_type = random.choice(['advcl', 'ccomp', 'xcomp', 'nsubj', 'csubj'])
        if re.search('rse', row_forms[imperative_titles.index('infinitive')]) is not None:
            reflexive_verb = row_forms[imperative_titles.index('infinitive')]
            infinitive_verb = reflexive_verb[:-2]
            mwt_token = row_forms[imperative_titles.index(form)]
            if cap == 1:
                mwt_token = mwt_token.capitalize()
            submitted_text = text + mwt_token + "."
            mwt_text = "1-2\t" + mwt_token + "\t_\t_\t_\t_\t_\t_\t_\tSpaceAfter=No"
            conj_verb = mwt_token[:-2]
            conj_verb = conj_verb.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú',
                                                                                                                  'u')
            if form == 'tu':
                verb = "1\t" + conj_verb + "\t" + infinitive_verb + \
                       "\tVERB\t_\tMood=Imp|Numb=Sing|Person=2|VerbForm=Fin\t0\t" + clause_type + "\t_\t_"
                add_pron = random.choice(reflex_te)
            elif form == 'usted':
                verb = "1\t" + conj_verb + "\t" + infinitive_verb + \
                       "\tVERB\t_\tMood=Imp|Numb=Sing|Person=3|VerbForm=Fin\t0\t" + clause_type + "\t_\t_"
                add_pron = random.choice(reflex_se)
            else:
                verb = "1\t" + conj_verb + "\t" + infinitive_verb + \
                       "\tVERB\t_\tMood=Imp|Numb=PLur|Person=3|VerbForm=Fin\t0\t" + clause_type + "\t_\t_"
                add_pron = random.choice(reflex_se)
        else:
            infinitive_verb = row_forms[imperative_titles.index('infinitive')]
            conj_verb = row_forms[imperative_titles.index(form)]
            syllables = 0
            i = len(conj_verb) - 1
            while i >= 0:
                if conj_verb[i] in ['a', 'e', 'i', 'o', 'u']:
                    if conj_verb[i] == 'u' and conj_verb[i + 1] in ['e', 'i']:
                        pass
                    else:
                        syllables += 1
                        if syllables == 2:
                            break
                i -= 1
            if i >= 0:
                mwt_verb = conj_verb[:i] + accent_letter[conj_verb[i].lower()] + conj_verb[i + 1:]
            else:
                mwt_verb = conj_verb
            add_pron = random.choice(con_obj_add)
            mwt_pron = re.findall(r'[\d]+\t([A-Za-z]+)\t', add_pron)[0]
            mwt_token = mwt_verb + mwt_pron
            if cap == 1:
                mwt_token = mwt_token.capitalize()
                conj_verb = conj_verb.capitalize()
            submitted_text = text + mwt_token + "."
            mwt_text = "1-2\t" + mwt_token + "\t_\t_\t_\t_\t_\t_\t_\tSpaceAfter=No"
            if form == 'tu':
                verb = "1\t" + conj_verb + "\t" + infinitive_verb + \
                       "\tVERB\t_\tMood=Imp|Numb=Sing|Person=2|VerbForm=Fin\t0\t" + clause_type + "\t_\t_"
            elif form == 'usted':
                verb = "1\t" + conj_verb + "\t" + infinitive_verb + \
                       "\tVERB\t_\tMood=Imp|Numb=Sing|Person=3|VerbForm=Fin\t0\t" + clause_type + "\t_\t_"
            else:
                verb = "1\t" + conj_verb + "\t" + infinitive_verb + \
                       "\tVERB\t_\tMood=Imp|Numb=PLur|Person=3|VerbForm=Fin\t0\t" + clause_type + "\t_\t_"

        text_parts = [sent_id, submitted_text, mwt_text, verb, add_pron, period_dir]
        new_entry = '\n'.join(text_parts)
        if new_entry not in mwt_strings:
            mwt_strings.append(new_entry)

with open('spanish.mwt', mode='wt', encoding='utf-8') as file:
    file.write('\n\n'.join(mwt_strings))
