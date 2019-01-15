from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("snakes"))
print(lemmatizer.lemmatize("photosynthesis"))
print(lemmatizer.lemmatize("thieves"))
print(lemmatizer.lemmatize("Brooks"))