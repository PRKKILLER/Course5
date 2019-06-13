import pymongo 
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.porter import PorterStemmer
import json
porter = PorterStemmer()
stems = []
new_stop_words=["'s","...",".","&"]
stop_words = stopwords.words("english")
stop_words.extend(new_stop_words)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["amamzon"]
#print(myclient.list_database_names())
mycol = mydb["Product"]
#print(mydb.list_collection_names())
x=mycol.find_one({},{"Reviews":1,"_id":0})
data=x["Reviews"]



########################
bucket={'battery': ['battery', 'batterylife', 'batteries',"charge","life","heat"],
    'picture': [ 'camera', 'pictures', 'pic', 'photo', 'photograph', 'photography','selfie'],
    'value': ['worth', 'value', 'cheap','amazing'],
    'sound': ['sound', 'music', 'speaker', 'loud', 'volume'],
    'fingerprint': ['fingerprint', 'scanner', 'finger','sensor'],    
  }
newdict={}
for key,value in bucket.items():
    l=[]
    for i in value:
        l.append(porter.stem(i))   
    newdict[key]=l
#print(newdict)

#########################

review_bucket={'battery': [],
    'picture': [],
    'value': [],
    'sound': [],
    'fingerprint': [],    
  }
for key,value in newdict.items():
    #print("key",key)
    for l in value:
        #print(l)
        for i in data:
            tokens = word_tokenize(i)
            tokens = [porter.stem(w).lower() for w  in tokens if not (w in stop_words) and w.isalnum()]
            #print("sentence",i)
            for j in tokens:
                #print("word",j)
                if j==l:
                    review_bucket[key].append(i)
                    break
#print(review_bucket)

#print Summary
for key,value in review_bucket.items():
    print(key,len(value))


tops = json.dumps(review_bucket)
out = open('classify.json', 'w')
out.write(tops)
