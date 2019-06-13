from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
import json

with open("classify.json", "r") as read_file:
    data = json.load(read_file)

sid = SentimentIntensityAnalyzer()

sentimentbucket={'battery': {},
    'picture': {},
    'value': {},
    'sound': {},
    'fingerprint': {},    
  }
sentiment=[]
##################for key,sentences in data.items():
for key,sentences in data.items():
    for sentence in sentences:
        #print(sentence)
        ss = sid.polarity_scores(sentence)
        for k in sorted(ss):
            #print(ss[k] ," ", k +" ")
        try:        
            sentimentbucket[key]["num"]=sentimentbucket[key]["num"]+1
        except KeyError :
            sentimentbucket[key]["num"]=1    
        
        if(ss["compound"]>0.05):
            print("Positive Overall ")
            try:        
                sentimentbucket[key]["pos"]=sentimentbucket[key]["pos"]+1
            except KeyError :
                sentimentbucket[key]["pos"]=1
        elif(ss["compound"]>-0.05) and (ss["compound"]<0.05):
            print("Neutral Overall")
            try:        
                sentimentbucket[key]["neu"]=sentimentbucket[key]["new"]+1
            except KeyError :
                sentimentbucket[key]["neu"]=1
        elif(ss["compound"]<-0.05):
            print("Negative Overall")
            try:        
                sentimentbucket[key]["neg"]=sentimentbucket[key]["neg"]+1
            except KeyError :
                sentimentbucket[key]["neg"]=1
          
    #print(sentimentbucket,key)
    #print(sentimentbucket[key])
    try:        
        sentimentbucket[key]["neg"]=sentimentbucket[key]["neg"]/sentimentbucket[key]["num"]*100
    except KeyError :
            sentimentbucket[key]["neg"]=0
    try:        
        sentimentbucket[key]["pos"]=sentimentbucket[key]["pos"]/sentimentbucket[key]["num"]*100
    except KeyError :
        sentimentbucket[key]["pos"]=0
    try:        
        sentimentbucket[key]["neu"]=sentimentbucket[key]["neu"]/sentimentbucket[key]["num"]*100
    except KeyError :
        sentimentbucket[key]["neu"]=0
 
#print(sentimentbucket)


#! pip install pywaffle
# Reference: https://stackoverflow.com/questions/41400136/how-to-do-waffle-charts-in-python-square-piechart
import csv

with open('sentiments.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #way to write to csv file
    writer.writerow(['Sentiment','Battery','Picture','Sound','Value','Fingerprint'])
    writer.writerow(['Positive',int(sentimentbucket['battery']["pos"]),int(sentimentbucket['picture']["pos"]),int(sentimentbucket['sound']["pos"]),int(sentimentbucket['value']["pos"]),int(sentimentbucket['fingerprint']["pos"])])
    writer.writerow(['Negative',int(sentimentbucket['battery']["neg"]),int(sentimentbucket['picture']["neg"]),int(sentimentbucket['sound']["neg"]),int(sentimentbucket['value']["neg"]),int(sentimentbucket['fingerprint']["neg"])])
    writer.writerow(['Neutral',int(sentimentbucket['battery']["neu"]),int(sentimentbucket['picture']["neu"]),int(sentimentbucket['sound']["neu"]),int(sentimentbucket['value']["neu"]),int(sentimentbucket['fingerprint']["neu"])])
   


