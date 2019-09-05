from nltk.corpus import stopwords
stop_words = set(stopwords.words(‘english’)) 
lines_without_stopwords=[] 
import WordNet Lemmatizer from nltk 
from nltk.stem import WordNetLemmatizer
 wordnet_lemmatizer = WordNetLemmatizer() 
for key,value in data.items
    lines=data[key]
    lines_without_stopwords=[]
    for line in lines:
        temp_line=[]
        for word in line:
            if word not in stop_words:
                temp_line.append(word)
        string=" "
        lines_without_stopwords.append(string.join(temp_line)) 
    data[key]=lines_without_stopwords             
import json
with open('path_to_file/person.json') as f:
  data = json.load(f)