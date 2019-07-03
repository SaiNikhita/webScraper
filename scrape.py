from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import os
basedir=os.path.abspath(os.path.dirname(__file__))


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqllite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Comm(db.Model):
	__tablename__='Comment_base'

	id=db.Column(db.Integer,primary_key=True)
	Comment=db.Column(db.Text)


	def __init__(self,Comment):
		self.Comment= Comment


@app.route("/profile")
def profile():
	return render_template("profiles.html")
if __name__=="__main__":
	app.run()


"""import requests
import sys
import nltk
import string
import scipy.sparse
import profanity
from profanity import profanity
#from nltk import pos_tag
#from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import wordnet
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
#import gensim
#from gensim import corpora, models
from bs4 import BeautifulSoup
#import gensim
#from gensim import corpora, models
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
import nltk
import string
import re
from nltk.stem import wordnet
from nltk.corpus import stopwords
from urllib.request import urlopen
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np

page = requests.get("https://www.desidime.com/stores/amazon-india/reviews")
print(page)
print(page.status_code)
print(page.content)
import os

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
reviews=soup.find_all('div',attrs={'class':'f14 csecondary mb10'})
l=list()
com=""
print(len(reviews))
for rev in range(len(reviews)):
	if rev!=7:
		com=(reviews[rev].text)
		l.append(com)
	
print(l)
stop_words = set(stopwords.words('english'))

new_com=[]
for i in l:
	print(i)
	r=re.split('[^a-zA-Z]',i)
	sen=""
	for w in r:
		print(w)
		if w.lower() not in stop_words and w not in string.punctuation:
			sen=sen+w+' '
	new_com.append(sen)
print(new_com)
vect = TfidfVectorizer(min_df=1)
tfidf = vect.fit_transform(new_com) #each sentence can be replaced by a whole document
print((tfidf * tfidf.T).A)
feature_names = vect.get_feature_names()
doc = 0
feature_index = tfidf[doc,:].nonzero()[1]
tfidf_scores = zip(feature_index, [tfidf[doc, x] for x in feature_index])
max=0
for w, s in [(feature_names[i], s) for (i, s) in tfidf_scores]:
	if s>max:
		max=s
		word=w
	print( w, s)
print(word,max)
index=0
m=[]
for i in l:
	if word in l[index]:
		m.append(l[index])
	index=index+1
print(m)
tokens1=list()
tokens2=list()

tokenizer=nltk.tokenize.punkt.PunktSentenceTokenizer()
for i in range(len(m)):
	tokens=tokenizer.tokenize(m[i])
	#tokens2=tokens2+word_tokenize(str(tokens))
	tokens1.append(tokens)
print('\n\n\nSentence tokens',tokens1)

for i in tokens1:
	tokens2=tokens2+i[0].split()

print('\n\n\nWord tokens',tokens2)

filtered_sentence = []
for w in tokens2:
    if w.lower() not in stop_words and w not in string.punctuation:
        filtered_sentence.append(w)
print('\n\n\nFiltered tokens',filtered_sentence)

my_new_string=[]
for w in filtered_sentence:
	my_new_string =my_new_string+ re.split('[^a-zA-Z]',w)	
print('\n\n\n',my_new_string)

filtered_sentence1 = []
for w in my_new_string:
    if w.lower() not in stop_words and w not in string.punctuation:
        filtered_sentence1.append(w)
print('\n\n\nFiltered tokens',filtered_sentence1)
str=""
for i in filtered_sentence1:
	str=str+" "+i
print(str)



# plot a line, implicitly creating a subplot(111)
plt.plot([1,2,3])
# now create a subplot which represents the top plot of a grid
# with 2 rows and 1 column. Since this subplot will overlap the
# first, the plot (and its axes) previously created, will be removed
plt.subplot(211)
wordcloud = WordCloud(width=6000,height=2000).generate(str)
plt.imshow(wordcloud, interpolation="bilinear")
plt.subplot(212)
label=['Positive','Negetive']
percentage=[50,20]
index = np.arange(len(label))
plt.bar(index,percentage)
plt.savefig("plots.png")
plt.show()"""