from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

os = PorterStemmer()

exp_words = ["python", "pythoning", "pythoned", "pythoner", "pythonly"]

#for w in exp_words:
 #   print(os.stem(w))
 
new = "It is very important to be pyhtonly while you are pythoning with pyhton. All pyhtoners have pythoned poorly at least once. "

words = word_tokenize(new)

for w in words:
    print(os.stem(w))