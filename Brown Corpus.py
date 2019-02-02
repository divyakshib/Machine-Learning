from nltk.corpus import brown,stopwords
from nltk.tokenize import sent_tokenize,word_tokenize,RegexpTokenizer
from nltk.stem.snowball import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
print(brown.categories())
data=brown.sents(categories='fiction')[:10]
print(data)
#tokenize
text="Opera refers to a dramatic art form, originating in Europe, in which the emotional content is conveyed to the audience as much through music, both vocal and instrumental, as it is through the lyrics. By contrast, in musical theater an actor's dramatic performance is primary, and the music plays a lesser role. The drama in opera is presented using the primary elements of theater such as scenery, costumes, and acting. However, the words of the opera, or libretto, are sung rather than spoken. The singers are accompanied by a musical ensemble ranging from a small instrumental ensemble to a full symphonic orchestra."
sent=sent_tokenize(text)
words=word_tokenize(sent[0])
#stopwords
sw=set(stopwords.words("english"))
print(sw)
def remove_stopwords(words):
    wor=[w for w in words if w not in sw]
    return(wor)
def tokenizer_(text):
    token=RegexpTokenizer("[a-zA-Z]+")
    word=token.tokenize(text)
    word_list=remove_stopwords(word)
    ps=PorterStemmer()
    tokenized=[]
    tokenized=[ps.stem(w) for w in word_list if ps.stem(w) not in tokenized ]
    return(tokenized)
corpus=["Opera refers to a dramatic art form, originating in Europe, in which the emotional content is conveyed to the audience as much through music, both vocal and instrumental, as it is through the lyrics. By contrast, in musical theater an actor's dramatic performance is primary, and the music plays a lesser role."
      "The drama in opera is presented using the primary elements of theater such as scenery, costumes, and acting. However, the words of the opera, or libretto, are sung rather than spoken."
      "The singers are accompanied by a musical ensemble ranging from a small instrumental ensemble to a full symphonic orchestra."]
cv=CountVectorizer(tokenizer=tokenizer_, ngram_range=(1,2))
vector=cv.fit_transform(corpus).todense()

print(cv.vocabulary_)
print(vector)
print(cv.inverse_transform(vector[0]))
from sklearn.feature_extraction.text import TfidfVectorizer
tf=TfidfVectorizer(norm='l2', tokenizer=tokenizer_,ngram_range=(1,2))
vectorized=tf.fit_transform(corpus).toarray()
print(vectorized)