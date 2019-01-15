import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train = state_union.raw("2005-GWBush.txt")
sample = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train)

tokenized = custom_sent_tokenizer.tokenize(sample)

def process_conten():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            #print(tagged)
            
            chunkGram = r"""Chunk: {<.*>+}
                                    }<VB.?|IN|DT>+{"""
            
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            
            chunked.draw()
            
            
            
            
            
    except Exception as e:
            print(str(e))
            
            
process_conten()