import os
import re
from nltk.corpus import stopwords
from nltk.corpus import sentiwordnet
import sys
import nltk
import string
import scipy.sparse
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import wordnet
stop_words = set(stopwords.words('english'))
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pymysql
from urllib.request import urlopen
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np

positive=[]
posper=[]
negper=[]
def split_line(line):
    cols = line.split("\t")
    return cols

def get_words(cols):
    words_ids = cols[4].split(" ")
    words = [w.split("#")[0] for w in words_ids]
    return words

def get_positive(cols):
    return cols[2]

def get_negative(cols):
    return cols[3]

def get_objective(cols):
    return 1 - (float(cols[2]) + float(cols[3]))

def get_gloss(cols):
    return cols[5]

def get_scores(filepath, sentiword):

    f = open(filepath)
    totalobject =0.0
    count =0.0
    totalpositive =0.0
    totalnegative =0.0
    for line in f:
        if not line.startswith("#"):
            cols = split_line(line)
            words = get_words(cols)
           # print(words)
            
            for word in sentiword:

                if word in words:
                    if word == "not":
                        totalobject = totalobject + 0
                        totalpositive = totalpositive + 0
                        totalnegative = totalnegative + 16
                        count =count + 1
                    else:

                        #print("For given word {0} - {1}".format(word, get_gloss(cols)))
                        #print("P Score: {0}".format(get_positive(cols)))
                        #print("N Score: {0}".format(get_negative(cols)))
                        #print("O Score: {0}\n".format(get_objective(cols)))
                        totalobject = totalobject + get_objective(cols)
                        totalpositive = totalpositive + float(get_positive(cols))
                        totalnegative = totalnegative + float(get_negative(cols))
                        count =count + 1
    if count >0:
        if totalpositive > totalnegative :
            positive.append(1)
            posper.append(totalpositive)            
            print("Positive word : 1")
            print("Positive value : ",totalpositive)
            print("Negative value : ",totalnegative)
        else :
            positive.append(-1)
            negper.append(totalnegative)
            print("Negative : -1")
            print("Positive value : ",totalpositive)
            print("Negative value : ",totalnegative)

        print("average object Score : ",totalobject/count)

            

if __name__ == "__main__":
    html=urlopen("http://www.desidime.com/stores/amazon-india/reviews").read()
    soup=BeautifulSoup(html)
    reviews=soup.find_all('div',attrs={'class':'f14 csecondary mb10'})
    l=list()
    com=""
    print(len(reviews))
    for rev in range(len(reviews)):
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
    tokens1=list()
    tokens2=list()

    tokenizer=nltk.tokenize.punkt.PunktSentenceTokenizer()
    for i in range(len(l)):
        tokens=tokenizer.tokenize(l[i])
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
    for i in l:
        comment = i
        sentiword = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", comment).split())
        stop_words = set(stopwords.words('english'))
    
        sentiword = sentiword.lower().split(" ")
        filtered_sentence = [w for w in sentiword  if not w in stop_words ]
    #print(filtered_sentence)
        get_scores("SentiWordNet_3.0.0_20130122.txt",filtered_sentence)
    print(positive)
    posi=sum(posper)/len(posper)
    negi=sum(negper)/len(negper)
    print(posi,negi)
    poscom=[]
    for i in range(len(l)):
        if positive[i]==1:
            poscom.append(l[i])
    print(poscom)
    if os.path.exists("plots.png"):
    	os.remove("plots.png")
    plt.plot([1,2,3])
    plt.subplot(211)
    wordcloud = WordCloud(width=6000,height=2000).generate(str)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.subplot(212)
    label=['Positive','Negetive']
    percentage=[posi,negi]
    index = np.arange(len(label))
    plt.bar(index,percentage)
    plt.savefig("plots.png")

#{% include 'profiless.html' %}
from flask import Flask,render_template,url_for
app=Flask(__name__)
@app.route('/profile')
def profile():
	{% include 'profiless.html' %}
	#return render_template("profiless.html",result=poscom,)
if __name__=="__main__":
	app.run()