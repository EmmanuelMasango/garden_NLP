# =====IMPORTS=====
import spacy

nlp = spacy.load('en_core_web_sm')

gardenpathSentences = [
    'The man pushed through the door fell.',
    'I told the girl the cat scratched Bill would help her.',
    'Mary gave the child a Band-Aid.',
    'That Jill is never here hurts.',
    'The cotton clothing is made of grows in Mississippi.'
]

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    tokenizedDoc = [token.orth_ for token in doc]
    recognisedDoc = [(i, i.label_,) for i in doc.ents]
    print("Original Sentence:", sentence)
    print("Tokenized sentence:", tokenizedDoc)
    print("Recognized entities:", recognisedDoc, '\n')

print("GPE: " + spacy.explain("GPE"))
print("PERSON: " + spacy.explain("PERSON"))

# 1. GPE stands for Geo-Political Entities
# The explanation for GPE is correct since Mississippi is a state in the Southeastern region of the United States.

# 2. The explanation for PERSON was correct since Jill Mary and Bill are names that could belong to an individual.
