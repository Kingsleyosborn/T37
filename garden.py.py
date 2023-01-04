

# Create the file garden.py for this task.
# 1. Use some Garden Path sentences or think up your own (at least 5).
# 2. Tokenise and perform Entity recognition for each of the sentences
#    after you have stored them in a list called gardenpathSentences.
# 3. See how spaCy has categorised these sentences and look up the entities you
#    don't understand
# 4. At the bottom of your file, write a comment about two unusual entities
# you found that spaCy gave one of the words of your sentences - did you expect this?

import spacy
NER = spacy.load("en_core_web_sm")
gardenpathSentences = []
print("************************************************************************")

raw_text_1 = "Sally sat on the mat which was on the floor, "
text_1 = NER(raw_text_1)
print([token.orth_ for token in text_1 if not token.is_punct | token.is_space])
for word in text_1.ents:
    print(word.text,word.label_)
print([(i, i.label_, i.label) for i in text_1.ents])
gardenpathSentences.append([token.orth_ for token in text_1 if not token.is_punct | token.is_space])

print("************************************************************************")

raw_text_2 = "Sir Jordan meet you at the restaurant at noon, not the café."
text_2 = NER(raw_text_2)
print([token.orth_ for token in text_2 if not token.is_punct | token.is_space])
for word in text_2.ents:
    print(word.text,word.label_)
print([(i, i.label_, i.label) for i in text_2.ents])
gardenpathSentences.append([token.orth_ for token in text_2 if not token.is_punct | token.is_space])
print("************************************************************************")

raw_text_3 = "Miss Dorry handed out the homework, which was due the next day."
text_3 = NER(raw_text_3)
print([token.orth_ for token in text_3 if not token.is_punct | token.is_space])
for word in text_3.ents:
    print(word.text,word.label_)
print([(i, i.label_, i.label) for i in text_3.ents])
gardenpathSentences.append([token.orth_ for token in text_3 if not token.is_punct | token.is_space])
print("************************************************************************")


raw_text_4 = "Peter's kids were playing in Central park, which was across avenue 5 from the library."
text_4 = NER(raw_text_4)
print([token.orth_ for token in text_4 if not token.is_punct | token.is_space])
for word in text_4.ents:
    print(word.text,word.label_)
print([(i, i.label_, i.label) for i in text_4.ents])
gardenpathSentences.append([token.orth_ for token in text_4 if not token.is_punct | token.is_space])
print("************************************************************************")

raw_text_5 = "The bus driver signaled to the pedestrian that it was safe to cross the street."
text_5 = NER(raw_text_5)
print([token.orth_ for token in text_5 if not token.is_punct | token.is_space])
for word in text_5.ents:
    print(word.text,word.label_)
print([(i, i.label_, i.label) for i in text_5.ents])
gardenpathSentences.append([token.orth_ for token in text_5 if not token.is_punct | token.is_space])
print("************************************************************************")

print(gardenpathSentences)

#spaCy thought sentence 4 the 5 in avenue 5 is CARDINAL. But in fact avenue 5 is a location
#spaCy return empty list which it does not catagorize any of those words.