###############################################################################
# Part 3: NER 
###############################################################################
import spacy
nlp = spacy.load('en_core_web_md') # python -m spacy download en

def ner_info(doc):
    print("\n" + "-" * 20)
    print("entities:")
    print(doc.ents)
    print("\n")
    for ent in doc.ents:
        print(ent.label_, ent.text)

text = open('shakes/shakes1.txt').read()
print(text)
doc2 = nlp(text)
#doc1 = nlp(u'London is a big city in the United Kingdom.')
#doc2 = nlp(u'While in France, Christine Lagarde discussed short-term stimulus efforts in a '
#           u'recent interview on 5:00 P.M. with the Wall Street Journal')
#ner_info(doc1)
ner_info(doc2)
