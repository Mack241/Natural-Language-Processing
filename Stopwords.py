from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "One of the first steps to pre-processing is to utilize stop-words. Stop words are words that you want to filter out of any analysis. These are words that carry no meaning, or carry conflicting meanings that you simply do not want to deal with. "
stop_words = set(stopwords.words("english"))

words = word_tokenize(text)

filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
    
print (filtered_sentence)